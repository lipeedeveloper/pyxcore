import unittest
from pyxcore.compiler.lexer import Lexer
from pyxcore.compiler.parser import Parser
from pyxcore.compiler.ast_nodes import Program
class TestLexerParser(unittest.TestCase):
    def test_parse_function(self):
        ast=Parser(Lexer('fn main() { print(\"ok\") }').tokenize()).parse()
        self.assertIsInstance(ast,Program)
if __name__=='__main__': unittest.main()
