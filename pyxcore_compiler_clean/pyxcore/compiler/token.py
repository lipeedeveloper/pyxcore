from dataclasses import dataclass
from enum import Enum

class TokenKind(str, Enum):
    EOF="EOF"; IDENT="IDENT"; NUMBER="NUMBER"; STRING="STRING"
    FN="FN"; LET="LET"; RETURN="RETURN"; IF="IF"; ELSE="ELSE"; WHILE="WHILE"
    TRUE="TRUE"; FALSE="FALSE"; NULL="NULL"
    LPAREN="LPAREN"; RPAREN="RPAREN"; LBRACE="LBRACE"; RBRACE="RBRACE"; COMMA="COMMA"; SEMICOLON="SEMICOLON"
    PLUS="PLUS"; MINUS="MINUS"; STAR="STAR"; SLASH="SLASH"; PERCENT="PERCENT"
    EQUAL="EQUAL"; EQEQ="EQEQ"; NE="NE"; GT="GT"; GTE="GTE"; LT="LT"; LTE="LTE"; BANG="BANG"; AND="AND"; OR="OR"

KEYWORDS = {"fn":TokenKind.FN, "let":TokenKind.LET, "return":TokenKind.RETURN, "if":TokenKind.IF, "else":TokenKind.ELSE, "while":TokenKind.WHILE, "true":TokenKind.TRUE, "false":TokenKind.FALSE, "null":TokenKind.NULL}

@dataclass(frozen=True)
class SourcePos:
    line:int
    col:int

@dataclass(frozen=True)
class Token:
    kind:TokenKind
    value:object
    pos:SourcePos
    def __repr__(self):
        return f"Token({self.kind.value}, {self.value!r}, {self.pos.line}:{self.pos.col})"
