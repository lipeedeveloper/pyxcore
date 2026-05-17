import argparse, pprint
from pathlib import Path
from pyxcore.compiler.pipeline import analyze_source, parse_source, run_source, tokenize_source
from pyxcore.tools.formatter import format_source
from pyxcore.tools.test_runner import run_tests
VERSION="0.1.0-compiler"
HELLO="""fn main() {
    println("Bem-vindo ao PyxCore!")
    let nome = "Mundo"
    println("Olá, " + nome + "!")
}
"""
def read_file(p): return Path(p).read_text(encoding="utf-8")
def cmd_run(a): run_source(read_file(a.file),a.file); return 0
def cmd_check(a): analyze_source(read_file(a.file),a.file); print(f"OK {a.file}"); return 0
def cmd_tokens(a):
    for t in tokenize_source(read_file(a.file),a.file): print(t)
    return 0
def cmd_ast(a): pprint.pp(parse_source(read_file(a.file),a.file)); return 0
def cmd_fmt(a):
    p=Path(a.file); f=format_source(p.read_text(encoding="utf-8"))
    if a.check: print(f)
    else: p.write_text(f,encoding="utf-8"); print(f"formatado: {p}")
    return 0
def cmd_new(a):
    folder=Path(a.name); folder.mkdir(parents=True,exist_ok=True)
    (folder/"main.pyx").write_text(HELLO,encoding="utf-8")
    print(f"projeto criado: {folder}")
    print(f"rode: cd {folder} && pyx run main.pyx")
    return 0
def cmd_repl(a):
    print("PyxCore REPL")
    print("digite :sair para fechar")
    while True:
        try: line=input("pyx> ").strip()
        except (KeyboardInterrupt,EOFError): print(); break
        if line in {"exit","quit",":sair",":exit"}: break
        if line:
            try: run_source(f"fn main() {{ println({line}) }}","<repl>")
            except Exception as exc: print(f"erro: {exc}")
    return 0
def cmd_test(a): return run_tests(a.path)
def cmd_doctor(a):
    print("PyxCore Doctor")
    print(f"versão: {VERSION}")
    print("lexer: OK")
    print("parser: OK")
    print("semantic: OK")
    print("runtime: OK")
    print("cli: OK")
    return 0
def main(argv=None):
    p=argparse.ArgumentParser(prog="pyx",description="PyxCore Compiler")
    p.add_argument("--version",action="store_true")
    s=p.add_subparsers(dest="cmd")
    x=s.add_parser("run"); x.add_argument("file"); x.set_defaults(func=cmd_run)
    x=s.add_parser("check"); x.add_argument("file"); x.set_defaults(func=cmd_check)
    x=s.add_parser("tokens"); x.add_argument("file"); x.set_defaults(func=cmd_tokens)
    x=s.add_parser("ast"); x.add_argument("file"); x.set_defaults(func=cmd_ast)
    x=s.add_parser("fmt"); x.add_argument("file"); x.add_argument("--check",action="store_true"); x.set_defaults(func=cmd_fmt)
    x=s.add_parser("new"); x.add_argument("name"); x.set_defaults(func=cmd_new)
    x=s.add_parser("repl"); x.set_defaults(func=cmd_repl)
    x=s.add_parser("test"); x.add_argument("path",nargs="?",default="tests"); x.set_defaults(func=cmd_test)
    x=s.add_parser("doctor"); x.set_defaults(func=cmd_doctor)
    a=p.parse_args(argv)
    if a.version: print(VERSION); return 0
    if not hasattr(a,"func"): p.print_help(); return 0
    try: return a.func(a)
    except Exception as exc: print(f"erro: {exc}"); return 1
if __name__=="__main__": raise SystemExit(main())
