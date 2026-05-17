from dataclasses import dataclass, field
from .ast_nodes import *
@dataclass
class SemanticResult: ok: bool; errors: list[str]=field(default_factory=list); warnings: list[str]=field(default_factory=list)
class Scope:
    def __init__(self,parent=None): self.parent=parent; self.symbols={}
    def define(self,n,k='var'):
        if n in self.symbols: return False
        self.symbols[n]=k; return True
    def resolve(self,n): return self.symbols.get(n) or (self.parent.resolve(n) if self.parent else None)
class SemanticAnalyzer:
    BUILTINS={'print','println','len','str','int','float','bool'}
    def analyze(self,program):
        self.errors=[]; self.warnings=[]; self.scope=Scope()
        for b in self.BUILTINS: self.scope.define(b,'builtin')
        self.visit(program); return SemanticResult(not self.errors,self.errors,self.warnings)
    def visit(self,n):
        if isinstance(n,Program):
            for x in n.body:
                if isinstance(x,FunctionDecl) and not self.scope.define(x.name,'function'): self.errors.append(f'Duplicate function: {x.name}')
            for x in n.body: self.visit(x)
        elif isinstance(n,FunctionDecl):
            old=self.scope; self.scope=Scope(old)
            for p in n.params: self.scope.define(p,'param')
            for s in n.body: self.visit(s)
            self.scope=old
        elif isinstance(n,VarDecl):
            if not self.scope.define(n.name,'var'): self.errors.append(f'Duplicate variable: {n.name}')
            self.visit(n.value)
        elif isinstance(n,Assign):
            if self.scope.resolve(n.name) is None: self.errors.append(f'Cannot assign undefined variable: {n.name}')
            self.visit(n.value)
        elif isinstance(n,Return): self.visit(n.value)
        elif isinstance(n,(IfStmt,WhileStmt)):
            self.visit(n.condition)
            for s in getattr(n,'then_body',getattr(n,'body',[])): self.visit(s)
            for s in getattr(n,'else_body',[]): self.visit(s)
        elif isinstance(n,ExprStmt): self.visit(n.expr)
        elif isinstance(n,Call):
            if self.scope.resolve(n.name) is None: self.errors.append(f'Undefined function: {n.name}')
            for a in n.args: self.visit(a)
        elif isinstance(n,Binary): self.visit(n.left); self.visit(n.right)
        elif isinstance(n,Identifier):
            if self.scope.resolve(n.name) is None: self.errors.append(f'Undefined variable: {n.name}')
