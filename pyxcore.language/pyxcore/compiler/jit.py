class LLVMJIT:
    def run(self,ir=None,return_value=0):
        try:
            from .llvm_backend import LlvmLiteBackend
            b=LlvmLiteBackend(); ir=ir or b.compile(return_value).optimized_ir; return b.jit_run_main_i32(ir)
        except Exception as exc: return {'ok':False,'reason':str(exc),'hint':"Install LLVM extras with: pip install -e '.[llvm]'"}
