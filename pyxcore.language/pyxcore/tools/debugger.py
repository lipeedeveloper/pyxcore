class Debugger:
    def __init__(self): self.breakpoints=set(); self.trace=[]
    def breakpoint(self,line): self.breakpoints.add(line); return f'breakpoint set at line {line}'
    def should_break(self,line): return line in self.breakpoints
    def record(self,event): self.trace.append(event)
