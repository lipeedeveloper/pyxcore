from dataclasses import dataclass, field
@dataclass
class Program: body:list=field(default_factory=list)
@dataclass
class FunctionDecl: name:str; params:list; body:list
@dataclass
class LetStmt: name:str; value:object
@dataclass
class AssignStmt: name:str; value:object
@dataclass
class ReturnStmt: value:object
@dataclass
class IfStmt: condition:object; then_body:list; else_body:list
@dataclass
class WhileStmt: condition:object; body:list
@dataclass
class ExprStmt: expr:object
@dataclass
class CallExpr: name:str; args:list
@dataclass
class BinaryExpr: left:object; op:str; right:object
@dataclass
class UnaryExpr: op:str; value:object
@dataclass
class LiteralExpr: value:object
@dataclass
class IdentifierExpr: name:str
