from pyxcore.compiler.lexer import Lexer
from pyxcore.compiler.parser import Parser
from pyxcore.compiler.semantic import SemanticAnalyzer
from pyxcore.runtime.interpreter import Interpreter
def tokenize_source(source,filename="<memory>"): return Lexer(source,filename).tokenize()
def parse_source(source,filename="<memory>"): return Parser(tokenize_source(source,filename),filename).parse()
def analyze_source(source,filename="<memory>"):
    p=parse_source(source,filename); SemanticAnalyzer().analyze(p); return p
def run_source(source,filename="<memory>"): return Interpreter().run(analyze_source(source,filename))
