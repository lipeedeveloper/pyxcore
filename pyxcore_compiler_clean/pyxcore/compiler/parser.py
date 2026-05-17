from .ast import *
from .errors import PyxSyntaxError
from .token import TokenKind

class Parser:
    def __init__(self, tokens, filename="<memory>"):
        self.tokens=tokens; self.filename=filename; self.i=0
    def parse(self):
        body=[]
        while not self.check(TokenKind.EOF): body.append(self.declaration())
        return Program(body)
    def declaration(self):
        if self.match(TokenKind.FN): return self.function()
        return self.statement()
    def function(self):
        name=self.consume(TokenKind.IDENT,"esperado nome da função").value
        self.consume(TokenKind.LPAREN,"esperado '('")
        params=[]
        if not self.check(TokenKind.RPAREN):
            params.append(self.consume(TokenKind.IDENT,"esperado parâmetro").value)
            while self.match(TokenKind.COMMA): params.append(self.consume(TokenKind.IDENT,"esperado parâmetro").value)
        self.consume(TokenKind.RPAREN,"esperado ')'")
        return FunctionDecl(name,params,self.block())
    def statement(self):
        if self.match(TokenKind.LET):
            name=self.consume(TokenKind.IDENT,"esperado nome da variável").value
            self.consume(TokenKind.EQUAL,"esperado '='")
            val=self.expression(); self.optional(TokenKind.SEMICOLON); return LetStmt(name,val)
        if self.match(TokenKind.RETURN):
            val=self.expression(); self.optional(TokenKind.SEMICOLON); return ReturnStmt(val)
        if self.match(TokenKind.IF):
            cond=self.expression(); then=self.block(); els=self.block() if self.match(TokenKind.ELSE) else []; return IfStmt(cond,then,els)
        if self.match(TokenKind.WHILE):
            cond=self.expression(); return WhileStmt(cond,self.block())
        expr=self.expression()
        if isinstance(expr,IdentifierExpr) and self.match(TokenKind.EQUAL):
            val=self.expression(); self.optional(TokenKind.SEMICOLON); return AssignStmt(expr.name,val)
        self.optional(TokenKind.SEMICOLON); return ExprStmt(expr)
    def block(self):
        self.consume(TokenKind.LBRACE,"esperado '{'")
        body=[]
        while not self.check(TokenKind.RBRACE) and not self.check(TokenKind.EOF): body.append(self.declaration())
        self.consume(TokenKind.RBRACE,"esperado '}'"); return body
    def expression(self): return self.logic_or()
    def logic_or(self):
        e=self.logic_and()
        while self.match(TokenKind.OR): e=BinaryExpr(e,"||",self.logic_and())
        return e
    def logic_and(self):
        e=self.equality()
        while self.match(TokenKind.AND): e=BinaryExpr(e,"&&",self.equality())
        return e
    def equality(self):
        e=self.comparison()
        while self.match(TokenKind.EQEQ,TokenKind.NE): e=BinaryExpr(e,self.previous().value,self.comparison())
        return e
    def comparison(self):
        e=self.term()
        while self.match(TokenKind.GT,TokenKind.GTE,TokenKind.LT,TokenKind.LTE): e=BinaryExpr(e,self.previous().value,self.term())
        return e
    def term(self):
        e=self.factor()
        while self.match(TokenKind.PLUS,TokenKind.MINUS): e=BinaryExpr(e,self.previous().value,self.factor())
        return e
    def factor(self):
        e=self.unary()
        while self.match(TokenKind.STAR,TokenKind.SLASH,TokenKind.PERCENT): e=BinaryExpr(e,self.previous().value,self.unary())
        return e
    def unary(self):
        if self.match(TokenKind.MINUS): return UnaryExpr("-",self.unary())
        if self.match(TokenKind.BANG): return UnaryExpr("!",self.unary())
        return self.call()
    def call(self):
        e=self.primary()
        while self.match(TokenKind.LPAREN):
            args=[]
            if not self.check(TokenKind.RPAREN):
                args.append(self.expression())
                while self.match(TokenKind.COMMA): args.append(self.expression())
            self.consume(TokenKind.RPAREN,"esperado ')'")
            if not isinstance(e,IdentifierExpr): raise self.error("somente identificadores podem ser chamados")
            e=CallExpr(e.name,args)
        return e
    def primary(self):
        if self.match(TokenKind.NUMBER,TokenKind.STRING): return LiteralExpr(self.previous().value)
        if self.match(TokenKind.TRUE): return LiteralExpr(True)
        if self.match(TokenKind.FALSE): return LiteralExpr(False)
        if self.match(TokenKind.NULL): return LiteralExpr(None)
        if self.match(TokenKind.IDENT): return IdentifierExpr(self.previous().value)
        if self.match(TokenKind.LPAREN):
            e=self.expression(); self.consume(TokenKind.RPAREN,"esperado ')'"); return e
        raise self.error("expressão esperada")
    def match(self,*kinds):
        if self.check(*kinds): self.i+=1; return True
        return False
    def check(self,*kinds): return self.peek().kind in kinds
    def consume(self,kind,msg):
        if self.check(kind):
            tok=self.peek(); self.i+=1; return tok
        raise self.error(msg)
    def optional(self,kind):
        if self.check(kind): self.i+=1
    def peek(self): return self.tokens[self.i]
    def previous(self): return self.tokens[self.i-1]
    def error(self,msg):
        tok=self.peek(); return PyxSyntaxError(f"{self.filename}:{tok.pos.line}:{tok.pos.col}: {msg}, veio {tok.kind.value}")
