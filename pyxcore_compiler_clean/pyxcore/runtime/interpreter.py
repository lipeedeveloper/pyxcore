from pyxcore.compiler.ast import *
from pyxcore.compiler.errors import PyxRuntimeError
class ReturnSignal(Exception):
    def __init__(self,value): self.value=value
class Environment:
    def __init__(self,parent=None): self.parent=parent; self.values={}
    def define(self,n,v): self.values[n]=v
    def assign(self,n,v):
        if n in self.values: self.values[n]=v; return
        if self.parent: self.parent.assign(n,v); return
        raise PyxRuntimeError(f"variável não definida: {n}")
    def get(self,n):
        if n in self.values: return self.values[n]
        if self.parent: return self.parent.get(n)
        raise PyxRuntimeError(f"nome não definido: {n}")
class Interpreter:
    def __init__(self):
        self.globals=Environment()
        self.globals.define("print",self._print); self.globals.define("println",self._print)
        self.globals.define("len",len); self.globals.define("str",str); self.globals.define("int",int); self.globals.define("float",float); self.globals.define("bool",bool)
    def run(self,program):
        for n in program.body:
            if isinstance(n,FunctionDecl): self.globals.define(n.name,n)
        try:
            main=self.globals.get("main")
            if isinstance(main,FunctionDecl): return self.call(main,[])
        except PyxRuntimeError: pass
        r=None
        for n in program.body:
            if not isinstance(n,FunctionDecl): r=self.exec(n,self.globals)
        return r
    def exec(self,n,e):
        if isinstance(n,FunctionDecl): e.define(n.name,n)
        elif isinstance(n,LetStmt): e.define(n.name,self.eval(n.value,e))
        elif isinstance(n,AssignStmt): e.assign(n.name,self.eval(n.value,e))
        elif isinstance(n,ReturnStmt): raise ReturnSignal(self.eval(n.value,e))
        elif isinstance(n,ExprStmt): return self.eval(n.expr,e)
        elif isinstance(n,IfStmt):
            local=Environment(e)
            for s in (n.then_body if self.truthy(self.eval(n.condition,e)) else n.else_body): self.exec(s,local)
        elif isinstance(n,WhileStmt):
            guard=0
            while self.truthy(self.eval(n.condition,e)):
                guard+=1
                if guard>1000000: raise PyxRuntimeError("loop excedeu limite de segurança")
                for s in n.body: self.exec(s,Environment(e))
        else: raise PyxRuntimeError(f"statement não suportado: {n}")
    def eval(self,n,e):
        if isinstance(n,LiteralExpr): return n.value
        if isinstance(n,IdentifierExpr): return e.get(n.name)
        if isinstance(n,UnaryExpr):
            v=self.eval(n.value,e)
            if n.op=="-": return -v
            if n.op=="!": return not self.truthy(v)
        if isinstance(n,BinaryExpr):
            if n.op=="&&": return self.truthy(self.eval(n.left,e)) and self.truthy(self.eval(n.right,e))
            if n.op=="||": return self.truthy(self.eval(n.left,e)) or self.truthy(self.eval(n.right,e))
            return self.bin(n.op,self.eval(n.left,e),self.eval(n.right,e))
        if isinstance(n,CallExpr):
            callee=e.get(n.name); args=[self.eval(a,e) for a in n.args]
            if isinstance(callee,FunctionDecl): return self.call(callee,args)
            if callable(callee): return callee(*args)
            raise PyxRuntimeError(f"{n.name} não é chamável")
        raise PyxRuntimeError(f"expressão não suportada: {n}")
    def call(self,fn,args):
        if len(args)!=len(fn.params): raise PyxRuntimeError(f"{fn.name} esperava {len(fn.params)} argumentos, recebeu {len(args)}")
        e=Environment(self.globals)
        for n,v in zip(fn.params,args): e.define(n,v)
        try:
            for s in fn.body: self.exec(s,e)
        except ReturnSignal as r: return r.value
    def bin(self,op,a,b):
        if op=="+": return str(a)+str(b) if isinstance(a,str) or isinstance(b,str) else a+b
        if op=="-": return a-b
        if op=="*": return a*b
        if op=="/": return a/b
        if op=="%": return a%b
        if op=="==": return a==b
        if op=="!=": return a!=b
        if op==">": return a>b
        if op==">=": return a>=b
        if op=="<": return a<b
        if op=="<=": return a<=b
        raise PyxRuntimeError(f"operador não suportado: {op}")
    def truthy(self,v): return bool(v)
    def _print(self,*values): print(" ".join(map(str,values)))
