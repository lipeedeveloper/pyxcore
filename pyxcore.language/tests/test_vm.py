import unittest
from pyxcore.vm.bytecode import BytecodeVM
class TestVM(unittest.TestCase):
    def test_vm_add(self): self.assertEqual(BytecodeVM().execute([('PUSH',2),('PUSH',3),('ADD',),('HALT',)]),5)
if __name__=='__main__': unittest.main()
