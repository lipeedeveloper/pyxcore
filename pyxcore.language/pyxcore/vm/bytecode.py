class BytecodeRuntimeError(RuntimeError): pass
class BytecodeVM:
    def __init__(self): self.stack=[]; self.locals={}; self.output=[]; self.builtins={'len':len,'str':str,'int':int,'float':float,'bool':bool}
    def execute(self,instructions):
        pc=0; self.stack.clear(); self.output.clear()
        while pc<len(instructions):
            ins=instructions[pc]; op=ins[0]
            if op=='PUSH': self.stack.append(ins[1])
            elif op=='POP': self.pop()
            elif op=='DUP': self.stack.append(self.peek())
            elif op=='LOAD': self.stack.append(self.locals[ins[1]])
            elif op=='STORE': self.locals[ins[1]]=self.pop()
            elif op in {'ADD','SUB','MUL','DIV','MOD','EQ','NE','LT','LTE','GT','GTE'}:
                b=self.pop(); a=self.pop(); self.stack.append(self.bin(op,a,b))
            elif op=='JMP': pc=int(ins[1]); continue
            elif op=='JMP_IF_FALSE':
                if not self.pop(): pc=int(ins[1]); continue
            elif op=='CALL_BUILTIN':
                name,argc=ins[1],int(ins[2]); args=[self.pop() for _ in range(argc)][::-1]; self.stack.append(self.builtins[name](*args))
            elif op=='PRINT': self.output.append(str(self.pop()))
            elif op=='HALT': break
            else: raise BytecodeRuntimeError(f'Unknown instruction: {op}')
            pc+=1
        return self.stack[-1] if self.stack else None
    def pop(self):
        if not self.stack: raise BytecodeRuntimeError('Stack underflow')
        return self.stack.pop()
    def peek(self):
        if not self.stack: raise BytecodeRuntimeError('Stack underflow')
        return self.stack[-1]
    def bin(self,op,a,b): return {'ADD':a+b,'SUB':a-b,'MUL':a*b,'DIV':a/b,'MOD':a%b,'EQ':a==b,'NE':a!=b,'LT':a<b,'LTE':a<=b,'GT':a>b,'GTE':a>=b}[op]
