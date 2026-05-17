class SSAOptimizer:
    def optimize(self,ins): return self.dead(self.copy(self.fold(ins)))
    def fold(self,ins):
        c={}; out=[]
        for x in ins:
            if x[0]=='const': c[x[1]]=x[2]; out.append(x)
            elif x[0] in {'add','sub','mul','div'} and isinstance(c.get(x[2]),(int,float)) and isinstance(c.get(x[3]),(int,float)):
                a,b=c[x[2]],c[x[3]]; v={'add':a+b,'sub':a-b,'mul':a*b,'div':a/b}[x[0]]; c[x[1]]=v; out.append(('const',x[1],v))
            else: out.append(x)
        return out
    def copy(self,ins): return ins
    def dead(self,ins): return ins
