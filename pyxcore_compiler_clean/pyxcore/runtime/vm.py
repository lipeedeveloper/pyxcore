from pyxcore.runtime.bytecode import Op
class VM:
    def __init__(self): self.stack=[]; self.vars={}
    def run(self,program):
        ip=0
        while ip<len(program.instructions):
            i=program.instructions[ip]
            if i.op==Op.CONST: self.stack.append(i.arg)
            elif i.op==Op.LOAD: self.stack.append(self.vars[i.arg])
            elif i.op==Op.STORE: self.vars[i.arg]=self.stack.pop()
            elif i.op==Op.ADD:
                b=self.stack.pop(); a=self.stack.pop(); self.stack.append(str(a)+str(b) if isinstance(a,str) or isinstance(b,str) else a+b)
            elif i.op==Op.PRINT: print(self.stack.pop())
            elif i.op==Op.HALT: break
            ip+=1
        return self.stack[-1] if self.stack else None
