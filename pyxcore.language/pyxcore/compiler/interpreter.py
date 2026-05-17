from .ast_nodes import *
class ReturnSignal(Exception):
    def __init__(self,v): self.value=v
class Env:
    def __init__(self,parent=None): self.parent=parent; self.values={}
    def define(self,n,v): self.values[n]=v
    def assign(self,n,v):
        if n in self.values: self.values[n]=v; return
        if self.parent: return self.parent.assign(n,v)
        raise NameError(f'Undefined variable: {n}')
    def get(self,n):
        if n in self.values: return self.values[n]
        if self.parent: return self.parent.get(n)
        raise NameError(f'Undefined variable: {n}')
class Interpreter:
    def __init__(self): self.globals=Env(); self.output=[]; self.globals.define('print',self._print); self.globals.define('println',self._print)
    def run(self,program):
        for x in program.body:
            if isinstance(x,FunctionDecl): self.globals.define(x.name,x)
        try: main=self.globals.get('main')
        except NameError: main=None
        if isinstance(main,FunctionDecl): return self._call(main,[])
        for x in program.body:
            if not isinstance(x,FunctionDecl): self.exec(x,self.globals)
    def exec(self,n,env):
        if isinstance(n,VarDecl): env.define(n.name,self.eval(n.value,env))
        elif isinstance(n,Assign): env.assign(n.name,self.eval(n.value,env))
        elif isinstance(n,Return): raise ReturnSignal(self.eval(n.value,env))
        elif isinstance(n,ExprStmt): self.eval(n.expr,env)
        elif isinstance(n,IfStmt):
            for s in (n.then_body if self.eval(n.condition,env) else n.else_body): self.exec(s,Env(env))
        elif isinstance(n,WhileStmt):
            guard=0
            while self.eval(n.condition,env):
                guard+=1
                if guard>100000: raise RuntimeError('Loop limit exceeded')
                for s in n.body: self.exec(s,Env(env))
    def eval(self,n,env):
        if isinstance(n,Literal): return n.value
        if isinstance(n,Identifier): return env.get(n.name)
        if isinstance(n,Binary): return self.bin(n.op,self.eval(n.left,env),self.eval(n.right,env))
        if isinstance(n,Call):
            fn=env.get(n.name); args=[self.eval(a,env) for a in n.args]
            return self._call(fn,args) if isinstance(fn,FunctionDecl) else fn(*args)
        raise RuntimeError(f'Unsupported node: {n}')
    def _call(self,fn,args):
        env=Env(self.globals)
        for n,v in zip(fn.params,args): env.define(n,v)
        try:
            for s in fn.body: self.exec(s,env)
        except ReturnSignal as r: return r.value
    def _print(self,v=''): self.output.append(str(v)); print(v)
    def bin(self,op,a,b):
        return {'+':a+b,'-':a-b,'*':a*b,'/':a/b,'%':a%b,'==':a==b,'!=':a!=b,'>':a>b,'>=':a>=b,'<':a<b,'<=':a<=b}[op]
