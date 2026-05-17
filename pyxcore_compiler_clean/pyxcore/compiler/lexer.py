from .errors import PyxSyntaxError
from .token import KEYWORDS, SourcePos, Token, TokenKind

TWO = {"==":TokenKind.EQEQ, "!=":TokenKind.NE, ">=":TokenKind.GTE, "<=":TokenKind.LTE, "&&":TokenKind.AND, "||":TokenKind.OR}
ONE = {"(":TokenKind.LPAREN, ")":TokenKind.RPAREN, "{":TokenKind.LBRACE, "}":TokenKind.RBRACE, ",":TokenKind.COMMA, ";":TokenKind.SEMICOLON, "+":TokenKind.PLUS, "-":TokenKind.MINUS, "*":TokenKind.STAR, "/":TokenKind.SLASH, "%":TokenKind.PERCENT, "=":TokenKind.EQUAL, ">":TokenKind.GT, "<":TokenKind.LT, "!":TokenKind.BANG}

class Lexer:
    def __init__(self, source, filename="<memory>"):
        self.source=source; self.filename=filename; self.i=0; self.line=1; self.col=1
    def tokenize(self):
        out=[]
        while not self.eof():
            c=self.peek()
            if c in " \t\r": self.advance(); continue
            if c=="\n": self.i+=1; self.line+=1; self.col=1; continue
            if c=="/" and self.peek(1)=="/":
                while not self.eof() and self.peek()!="\n": self.advance()
                continue
            if c.isalpha() or c=="_": out.append(self.ident()); continue
            if c.isdigit(): out.append(self.number()); continue
            if c in ("'", '"'): out.append(self.string()); continue
            two=c+self.peek(1)
            if two in TWO:
                pos=self.pos(); self.advance(); self.advance(); out.append(Token(TWO[two], two, pos)); continue
            if c in ONE:
                pos=self.pos(); self.advance(); out.append(Token(ONE[c], c, pos)); continue
            raise PyxSyntaxError(f"{self.filename}:{self.line}:{self.col}: caractere inesperado {c!r}")
        out.append(Token(TokenKind.EOF, "", self.pos()))
        return out
    def ident(self):
        pos=self.pos(); s=""
        while not self.eof() and (self.peek().isalnum() or self.peek()=="_"): s += self.advance()
        return Token(KEYWORDS.get(s, TokenKind.IDENT), s, pos)
    def number(self):
        pos=self.pos(); s=""; dot=False
        while not self.eof() and (self.peek().isdigit() or self.peek()=="."):
            if self.peek()==".":
                if dot: break
                dot=True
            s += self.advance()
        return Token(TokenKind.NUMBER, float(s) if dot else int(s), pos)
    def string(self):
        quote=self.advance(); pos=self.pos(); s=""
        while not self.eof() and self.peek()!=quote:
            if self.peek()=="\\":
                self.advance(); esc=self.advance()
                s += {"n":"\n","t":"\t","r":"\r","\\":"\\",'"':'"',"'":"'"}.get(esc,esc)
            else: s += self.advance()
        if self.eof(): raise PyxSyntaxError(f"{self.filename}:{pos.line}:{pos.col}: string não terminada")
        self.advance(); return Token(TokenKind.STRING, s, pos)
    def peek(self, off=0):
        j=self.i+off
        return "\0" if j>=len(self.source) else self.source[j]
    def advance(self):
        c=self.source[self.i]; self.i+=1; self.col+=1; return c
    def pos(self): return SourcePos(self.line,self.col)
    def eof(self): return self.i>=len(self.source)
