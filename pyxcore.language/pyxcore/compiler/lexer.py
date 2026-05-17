from dataclasses import dataclass
KEYWORDS={'fn':'FN','let':'LET','return':'RETURN','if':'IF','else':'ELSE','while':'WHILE','true':'TRUE','false':'FALSE','null':'NULL','match':'MATCH','case':'CASE','import':'IMPORT'}
TWO={'==':'EQEQ','!=':'NE','>=':'GTE','<=':'LTE','=>':'ARROW'}
ONE={'(':'LPAREN',')':'RPAREN','{':'LBRACE','}':'RBRACE','[':'LBRACKET',']':'RBRACKET',',':'COMMA',':':'COLON',';':'SEMICOLON','+':'PLUS','-':'MINUS','*':'STAR','/':'SLASH','%':'PERCENT','=':'EQUAL','>':'GT','<':'LT'}
@dataclass
class Token: type:str; value:object; line:int; column:int
class LexerError(SyntaxError): pass
class Lexer:
    def __init__(self,source): self.source=source; self.i=0; self.line=1; self.col=1
    def tokenize(self):
        out=[]
        while not self._eof():
            ch=self._peek()
            if ch in ' \t\r': self._adv(); continue
            if ch=='\n': self.i+=1; self.line+=1; self.col=1; continue
            if ch=='/' and self._peek(1)=='/':
                while not self._eof() and self._peek()!='\n': self._adv()
                continue
            if ch.isalpha() or ch=='_': out.append(self._ident()); continue
            if ch.isdigit(): out.append(self._num()); continue
            if ch in '"\'': out.append(self._str()); continue
            two=ch+self._peek(1)
            if two in TWO: out.append(Token(TWO[two],two,self.line,self.col)); self._adv(); self._adv(); continue
            if ch in ONE: out.append(Token(ONE[ch],ch,self.line,self.col)); self._adv(); continue
            raise LexerError(f'Unexpected character {ch!r} at {self.line}:{self.col}')
        out.append(Token('EOF','',self.line,self.col)); return out
    def _ident(self):
        l,c=self.line,self.col; v=''
        while not self._eof() and (self._peek().isalnum() or self._peek()=='_'): v+=self._adv()
        return Token(KEYWORDS.get(v,'IDENT'),v,l,c)
    def _num(self):
        l,c=self.line,self.col; v=''; dot=False
        while not self._eof() and (self._peek().isdigit() or self._peek()=='.'):
            if self._peek()=='.':
                if dot: break
                dot=True
            v+=self._adv()
        return Token('NUMBER',float(v) if dot else int(v),l,c)
    def _str(self):
        q=self._adv(); l,c=self.line,self.col; v=''
        while not self._eof() and self._peek()!=q:
            if self._peek()=='\\':
                self._adv(); e=self._adv(); v+={'n':'\n','t':'\t','"':'"',"'":"'",'\\':'\\'}.get(e,e)
            else: v+=self._adv()
        if self._eof(): raise LexerError(f'Unterminated string at {l}:{c}')
        self._adv(); return Token('STRING',v,l,c)
    def _peek(self,o=0):
        j=self.i+o; return '\0' if j>=len(self.source) else self.source[j]
    def _adv(self): ch=self.source[self.i]; self.i+=1; self.col+=1; return ch
    def _eof(self): return self.i>=len(self.source)
