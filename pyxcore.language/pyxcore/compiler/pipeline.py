from .lexer import Lexer
from .parser import Parser
from .semantic import SemanticAnalyzer
from .interpreter import Interpreter

def parse_source(source): return Parser(Lexer(source).tokenize()).parse()
def analyze_source(source): return SemanticAnalyzer().analyze(parse_source(source))
def run_source(source):
    ast=parse_source(source); res=SemanticAnalyzer().analyze(ast)
    if not res.ok: raise RuntimeError('\n'.join(res.errors))
    return Interpreter().run(ast)
