import argparse, unittest
from pathlib import Path
from .compiler.lexer import Lexer
from .compiler.parser import Parser
from .compiler.pipeline import run_source
from .compiler.formatter import format_source

def cmd_run(a): return run_source(Path(a.file).read_text(encoding='utf-8'))
def cmd_tokens(a):
    for t in Lexer(Path(a.file).read_text(encoding='utf-8')).tokenize(): print(t)
def cmd_ast(a): print(Parser(Lexer(Path(a.file).read_text(encoding='utf-8')).tokenize()).parse())
def cmd_fmt(a):
    p=Path(a.file); f=format_source(p.read_text(encoding='utf-8'))
    if a.check: print(f)
    else: p.write_text(f,encoding='utf-8'); print(f'formatted {p}')
def cmd_vm(a):
    from .vm.bytecode import BytecodeVM
    print(BytecodeVM().execute([('PUSH',a.a),('PUSH',a.b),('ADD',),('HALT',)]))
def cmd_jit(a):
    from .compiler.jit import LLVMJIT
    print(LLVMJIT().run(return_value=a.return_value))
def cmd_test(a):
    res=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.discover('tests',pattern='test*.py'))
    raise SystemExit(0 if res.wasSuccessful() else 1)
def cmd_publish(a):
    from .package_registry.client import RegistryClient
    print(RegistryClient(a.registry).publish(a.name,a.version,a.description,a.author))
def main(argv=None):
    p=argparse.ArgumentParser(prog='pyx',description='PyxCore CLI'); sub=p.add_subparsers(dest='cmd')
    x=sub.add_parser('run'); x.add_argument('file'); x.set_defaults(func=cmd_run)
    x=sub.add_parser('tokens'); x.add_argument('file'); x.set_defaults(func=cmd_tokens)
    x=sub.add_parser('ast'); x.add_argument('file'); x.set_defaults(func=cmd_ast)
    x=sub.add_parser('fmt'); x.add_argument('file'); x.add_argument('--check',action='store_true'); x.set_defaults(func=cmd_fmt)
    x=sub.add_parser('vm'); x.add_argument('a',type=int); x.add_argument('b',type=int); x.set_defaults(func=cmd_vm)
    x=sub.add_parser('jit'); x.add_argument('--return-value',type=int,default=0); x.set_defaults(func=cmd_jit)
    x=sub.add_parser('test'); x.set_defaults(func=cmd_test)
    x=sub.add_parser('publish'); x.add_argument('name'); x.add_argument('--version',default='0.1.0'); x.add_argument('--description',default=''); x.add_argument('--author',default=''); x.add_argument('--registry',default='http://127.0.0.1:8000'); x.set_defaults(func=cmd_publish)
    a=p.parse_args(argv)
    if not hasattr(a,'func'): p.print_help(); return 0
    return a.func(a)
if __name__=='__main__': main()
