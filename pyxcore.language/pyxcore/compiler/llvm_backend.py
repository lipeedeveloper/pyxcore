from dataclasses import dataclass
@dataclass
class LLVMBuildResult: ir:str; optimized_ir:str
class LLVMUnavailable(RuntimeError): pass
class LlvmLiteBackend:
    def __init__(self):
        try:
            import llvmlite.ir as ir; import llvmlite.binding as llvm
        except Exception as exc: raise LLVMUnavailable("llvmlite is not installed. Use: pip install -e '.[llvm]'") from exc
        self.ir=ir; self.llvm=llvm; llvm.initialize(); llvm.initialize_native_target(); llvm.initialize_native_asmprinter()
    def build_main_return_i32(self,value=0):
        ir=self.ir; m=ir.Module(name='pyx_module'); m.triple=self.llvm.get_default_triple(); f=ir.Function(m,ir.FunctionType(ir.IntType(32),[]),name='main'); b=f.append_basic_block(name='entry'); builder=ir.IRBuilder(b); builder.ret(ir.Constant(ir.IntType(32),int(value))); return str(m)
    def optimize(self,llvm_ir,opt_level=2):
        mod=self.llvm.parse_assembly(llvm_ir); mod.verify(); pmb=self.llvm.create_pass_manager_builder(); pmb.opt_level=opt_level; pm=self.llvm.create_module_pass_manager(); pmb.populate(pm); pm.run(mod); return str(mod)
    def compile(self,return_value=0):
        raw=self.build_main_return_i32(return_value); return LLVMBuildResult(raw,self.optimize(raw))
    def jit_run_main_i32(self,llvm_ir):
        import ctypes; target=self.llvm.Target.from_default_triple(); tm=target.create_target_machine(); engine=self.llvm.create_mcjit_compiler(self.llvm.parse_assembly(''),tm); mod=self.llvm.parse_assembly(llvm_ir); mod.verify(); engine.add_module(mod); engine.finalize_object(); ptr=engine.get_function_address('main'); return int(ctypes.CFUNCTYPE(ctypes.c_int32)(ptr)())
