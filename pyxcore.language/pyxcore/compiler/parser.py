from .ast_nodes import *
class ParserError(SyntaxError): pass
class Parser:
    def __init__(self,tokens): self.tokens=tokens; self.i=0
    def parse(self):
        body=[]
        while not self._check('EOF'): body.append(self._decl())
        return Program(body)
    def _decl(self): return self._function() if self._match('FN') else self._stmt()
    def _function(self):
        name=self._consume('IDENT','Expected function name').value; self._consume('LPAREN',"Expected '('"); params=[]
        if not self._check('RPAREN'):
            params.append(self._consume('IDENT','Expected parameter').value)
            while self._match('COMMA'): params.append(self._consume('IDENT','Expected parameter').value)
        self._consume('RPAREN',"Expected ')'"); return FunctionDecl(name,params,self._block())
    def _stmt(self):
        if self._match('LET'):
            n=self._consume('IDENT','Expected variable name').value; self._consume('EQUAL',"Expected '='"); v=self._expr(); self._optional('SEMICOLON'); return VarDecl(n,v)
        if self._match('RETURN'):
            v=self._expr(); self._optional('SEMICOLON'); return Return(v)
        if self._match('IF'):
            c=self._expr(); t=self._block(); e=self._block() if self._match('ELSE') else []; return IfStmt(c,t,e)
        if self._match('WHILE'):
            c=self._expr(); return WhileStmt(c,self._block())
        e=self._expr()
        if isinstance(e,Identifier) and self._match('EQUAL'):
            v=self._expr(); self._optional('SEMICOLON'); return Assign(e.name,v)
        self._optional('SEMICOLON'); return ExprStmt(e)
    def _block(self):
        self._consume('LBRACE',"Expected '{'"); b=[]
        while not self._check('RBRACE') and not self._check('EOF'): b.append(self._decl())
        self._consume('RBRACE',"Expected '}'"); return b
    def _expr(self): return self._equality()
    def _equality(self):
        e=self._comparison()
        while self._match('EQEQ','NE'): op=self._prev().value; e=Binary(e,op,self._comparison())
        return e
    def _comparison(self):
        e=self._term()
        while self._match('GT','GTE','LT','LTE'): op=self._prev().value; e=Binary(e,op,self._term())
        return e
    def _term(self):
        e=self._factor()
        while self._match('PLUS','MINUS'): op=self._prev().value; e=Binary(e,op,self._factor())
        return e
    def _factor(self):
        e=self._unary()
        while self._match('STAR','SLASH','PERCENT'): op=self._prev().value; e=Binary(e,op,self._unary())
        return e
    def _unary(self):
        if self._match('MINUS'): return Binary(Literal(0),'-',self._unary())
        return self._call()
    def _call(self):
        e=self._primary()
        while self._match('LPAREN'):
            args=[]
            if not self._check('RPAREN'):
                args.append(self._expr())
                while self._match('COMMA'): args.append(self._expr())
            self._consume('RPAREN',"Expected ')'")
            if not isinstance(e,Identifier): raise self._err('Can only call identifiers')
            e=Call(e.name,args)
        return e
    def _primary(self):
        if self._match('NUMBER','STRING'): return Literal(self._prev().value)
        if self._match('TRUE'): return Literal(True)
        if self._match('FALSE'): return Literal(False)
        if self._match('NULL'): return Literal(None)
        if self._match('IDENT'): return Identifier(self._prev().value)
        if self._match('LPAREN'):
            e=self._expr(); self._consume('RPAREN',"Expected ')'"); return e
        raise self._err('Expected expression')
    def _match(self,*ts):
        if self._check(*ts): self.i+=1; return True
        return False
    def _check(self,*ts): return self.tokens[self.i].type in ts
    def _optional(self,t):
        if self._check(t): self.i+=1
    def _consume(self,t,msg):
        if self._check(t): tok=self.tokens[self.i]; self.i+=1; return tok
        raise self._err(msg)
    def _prev(self): return self.tokens[self.i-1]
    def _err(self,msg): tok=self.tokens[self.i]; return ParserError(f'{msg} at {tok.line}:{tok.column}, got {tok.type}')
