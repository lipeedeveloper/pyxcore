from .ast import *
from .errors import PyxSemanticError
BUILTINS={"print","println","len","str","int","float","bool"}
class Scope:
    def __init__(self,parent=None): self.parent=parent; self.names=set()
    def define(self,n): self.names.add(n)
    def has_local(self,n): return n in self.names
    def resolve(self,n): return n in self.names or (self.parent and self.parent.resolve(n))
class SemanticAnalyzer:
    def analyze(self,program):
        s=Scope()
        for n in BUILTINS: s.define(n)
        for node in program.body:
            if isinstance(node,FunctionDecl):
                if s.has_local(node.name): raise PyxSemanticError(f"função já definida: {node.name}")
                s.define(node.name)
        for node in program.body: self.stmt(node,s,False)
    def stmt(self,node,s,in_fn):
        if isinstance(node,FunctionDecl):
            fs=Scope(s)
            for p in node.params:
                if fs.has_local(p): raise PyxSemanticError(f"parâmetro duplicado: {p}")
                fs.define(p)
            for x in node.body: self.stmt(x,fs,True)
        elif isinstance(node,LetStmt):
            self.expr(node.value,s)
            if s.has_local(node.name): raise PyxSemanticError(f"variável já definida: {node.name}")
            s.define(node.name)
        elif isinstance(node,AssignStmt):
            if not s.resolve(node.name): raise PyxSemanticError(f"variável não definida: {node.name}")
            self.expr(node.value,s)
        elif isinstance(node,ReturnStmt):
            if not in_fn: raise PyxSemanticError("return só pode ser usado dentro de função")
            self.expr(node.value,s)
        elif isinstance(node,ExprStmt): self.expr(node.expr,s)
        elif isinstance(node,IfStmt):
            self.expr(node.condition,s)
            for x in node.then_body: self.stmt(x,Scope(s),in_fn)
            for x in node.else_body: self.stmt(x,Scope(s),in_fn)
        elif isinstance(node,WhileStmt):
            self.expr(node.condition,s)
            loop=Scope(s)
            for x in node.body: self.stmt(x,loop,in_fn)
        else: raise PyxSemanticError(f"statement desconhecido: {node}")
    def expr(self,node,s):
        if isinstance(node,LiteralExpr): return
        if isinstance(node,IdentifierExpr):
            if not s.resolve(node.name): raise PyxSemanticError(f"nome não definido: {node.name}")
        elif isinstance(node,UnaryExpr): self.expr(node.value,s)
        elif isinstance(node,BinaryExpr): self.expr(node.left,s); self.expr(node.right,s)
        elif isinstance(node,CallExpr):
            if not s.resolve(node.name): raise PyxSemanticError(f"função não definida: {node.name}")
            for a in node.args: self.expr(a,s)
        else: raise PyxSemanticError(f"expressão desconhecida: {node}")
