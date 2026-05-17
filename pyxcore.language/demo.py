#!/usr/bin/env python3
"""
PyxCore Demo Script - Shows how the complete compiler works
Run this to see the full compilation pipeline in action
"""

import os
import sys
import subprocess
from pathlib import Path

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_section(title):
    """Print a section header"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{title:^60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}\n")

def print_code(code):
    """Print code sample"""
    print(f"{Colors.CYAN}{code}{Colors.ENDC}\n")

def print_success(msg):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {msg}{Colors.ENDC}")

def print_error(msg):
    """Print error message"""
    print(f"{Colors.RED}✗ {msg}{Colors.ENDC}")

def print_info(msg):
    """Print info message"""
    print(f"{Colors.BLUE}→ {msg}{Colors.ENDC}")

def demo_lexer():
    """Demonstrate the lexer"""
    print_section("LEXER DEMO - Tokenization")
    
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'compiler'))
    from lexer import Lexer, TokenType
    
    code = 'fn add(a: int, b: int) -> int { ret a + b }'
    print_info("Tokenizing PyxCore code:")
    print_code(code)
    
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    print_info("Generated tokens:")
    for token in tokens[:-1]:  # Skip EOF
        print(f"  {Colors.YELLOW}{token.type.name:15} {Colors.CYAN}{token.value:10}{Colors.ENDC}")
    
    print_success(f"Generated {len(tokens)-1} tokens (excluding EOF)")

def demo_parser():
    """Demonstrate the parser"""
    print_section("PARSER DEMO - Abstract Syntax Tree")
    
    from parser import parse_code
    from ast_nodes import FnDecl, VarDecl
    
    code = '''
    fn main() {
        let x: int = 10
        let y: int = 20
        print(x + y)
    }
    '''
    
    print_info("Parsing PyxCore code:")
    print_code(code)
    
    program = parse_code(code)
    
    print_info("Generated AST:")
    for stmt in program.statements:
        if isinstance(stmt, FnDecl):
            print(f"  {Colors.GREEN}Function: {stmt.name}{Colors.ENDC}")
            print(f"    Parameters: {len(stmt.params)}")
            print(f"    Body statements: {len(stmt.body)}")
        elif isinstance(stmt, VarDecl):
            print(f"  {Colors.GREEN}Variable: {stmt.name}{Colors.ENDC}")
            print(f"    Type: {stmt.type}")
    
    print_success(f"Generated AST with {len(program.statements)} statements")

def demo_type_checker():
    """Demonstrate the type checker"""
    print_section("TYPE CHECKER DEMO - Semantic Analysis")
    
    from parser import parse_code
    from type_checker import TypeChecker
    
    code = '''
    let x = 42
    let y: int = x
    let z: str = "hello"
    '''
    
    print_info("Checking types:")
    print_code(code)
    
    program = parse_code(code)
    checker = TypeChecker()
    
    try:
        program = checker.check_program(program)
        print_success("Type checking passed!")
        
        print_info("Inferred types:")
        for stmt in program.statements:
            if hasattr(stmt, 'name') and hasattr(stmt, 'type'):
                print(f"  {Colors.YELLOW}{stmt.name}: {stmt.type.name if hasattr(stmt.type, 'name') else stmt.type}{Colors.ENDC}")
    
    except Exception as e:
        print_error(f"Type error: {e}")

def demo_code_generator():
    """Demonstrate code generation"""
    print_section("CODE GENERATOR DEMO - C Code Generation")
    
    from parser import parse_code
    from type_checker import TypeChecker
    from codegen import CodeGen
    
    code = '''
    fn multiply(a: int, b: int) -> int {
        ret a * b
    }
    '''
    
    print_info("Input PyxCore code:")
    print_code(code)
    
    program = parse_code(code)
    checker = TypeChecker()
    program = checker.check_program(program)
    
    codegen = CodeGen()
    c_code = codegen.generate(program)
    
    print_info("Generated C code (excerpt):")
    lines = c_code.split('\n')
    for line in lines[-25:]:
        if line.strip():
            print(f"  {Colors.CYAN}{line}{Colors.ENDC}")
    
    print_success(f"Generated {len(c_code)} bytes of C code")

def demo_compilation():
    """Demonstrate full compilation"""
    print_section("FULL COMPILATION - PyxCore to Binary")
    
    # Create a simple test program
    test_dir = Path("demo_test")
    test_dir.mkdir(exist_ok=True)
    
    test_file = test_dir / "demo.pyx"
    test_file.write_text('''
fn factorial(n: int) -> int {
    if n <= 1 { ret 1 }
    ret n * factorial(n - 1)
}

fn main() {
    print("Factorial of 5: ")
    print(factorial(5))
}
''')
    
    print_info(f"Created test file: {test_file}")
    
    compiler_path = Path("compiler") / "pyxc.py"
    if compiler_path.exists():
        print_info("Compiling...")
        output_exe = test_dir / "demo"
        result = subprocess.run(
            [sys.executable, str(compiler_path), str(test_file), "-o", str(output_exe)],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print_success("Compilation successful!")
            
            # Show generated C file
            c_file = test_dir / "demo.c"
            if c_file.exists():
                with open(c_file) as f:
                    c_lines = f.readlines()
                print_info(f"Generated {len(c_lines)} lines of C code")
            
            # Try to run
            if output_exe.exists() or (output_exe.with_suffix('.exe')).exists():
                print_success("Binary created successfully!")
                exe_path = output_exe if output_exe.exists() else output_exe.with_suffix('.exe')
                print_info(f"Binary location: {exe_path}")
        else:
            print_error(f"Compilation failed: {result.stderr}")
    else:
        print_error(f"Compiler not found at {compiler_path}")

def main():
    """Run all demos"""
    print(f"{Colors.BOLD}{Colors.HEADER}")
    print("""
    ╔═══════════════════════════════════════════════════╗
    ║     PyxCore v2.0 - Complete Compiler Demo         ║
    ║  Systems-grade language with Python clarity       ║
    ╚═══════════════════════════════════════════════════╝
    """)
    print(f"{Colors.ENDC}")
    
    try:
        # Run demos
        demo_lexer()
        demo_parser()
        demo_type_checker()
        demo_code_generator()
        demo_compilation()
        
        print_section("DEMO COMPLETE")
        print_info("PyxCore compiler is working end-to-end!")
        print_info("Next steps:")
        print(f"  1. Read the documentation: {Colors.BOLD}GETTING_STARTED.md{Colors.ENDC}")
        print(f"  2. Try examples: {Colors.BOLD}cd examples && python ../pyx.py hello.pyx{Colors.ENDC}")
        print()
        
    except Exception as e:
        print_error(f"Demo failed: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
