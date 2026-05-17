import unittest
from pyxcore.compiler.pipeline import run_source
class TestInterpreter(unittest.TestCase):
    def test_return_math(self):
        src='fn soma(a,b){ return a+b } fn main(){ return soma(2,3) }'
        self.assertEqual(run_source(src),5)
if __name__=='__main__': unittest.main()
