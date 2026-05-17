from dataclasses import dataclass
from enum import Enum
class Op(str,Enum): CONST="CONST"; LOAD="LOAD"; STORE="STORE"; ADD="ADD"; PRINT="PRINT"; HALT="HALT"
@dataclass
class Instruction: op:Op; arg:object=None
class BytecodeProgram:
    def __init__(self): self.instructions=[]
    def emit(self,op,arg=None): self.instructions.append(Instruction(op,arg))
