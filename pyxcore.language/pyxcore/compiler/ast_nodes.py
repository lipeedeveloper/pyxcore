from dataclasses import dataclass, field
from typing import Any
@dataclass
class Program: body: list[Any] = field(default_factory=list)
@dataclass
class FunctionDecl: name: str; params: list[str]; body: list[Any]
@dataclass
class VarDecl: name: str; value: Any
@dataclass
class Assign: name: str; value: Any
@dataclass
class Return: value: Any
@dataclass
class IfStmt: condition: Any; then_body: list[Any]; else_body: list[Any] = field(default_factory=list)
@dataclass
class WhileStmt: condition: Any; body: list[Any]
@dataclass
class ExprStmt: expr: Any
@dataclass
class Call: name: str; args: list[Any]
@dataclass
class Binary: left: Any; op: str; right: Any
@dataclass
class Literal: value: Any
@dataclass
class Identifier: name: str
