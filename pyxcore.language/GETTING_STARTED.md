# Iniciando com PyxCore

Repositório: https://github.com/lipeedeveloper/pyxcore

Guia de introdução rápida para aprender PyxCore em 15 minutos.

**Criado por: Emanuel Felipe - Lipe Developer**

PyxCore é a base fundamental de uma nova geração de linguagens de programação, combinando segurança, performance e legibilidade.

## Seu Primeiro Programa

### 1. Crie `hello.pyx`

```pyx
fn main() {
    print("Olá, PyxCore!")
}
```

### 2. Compile

```bash
python pyx.py hello.pyx
```

### 3. Execute

```bash
./hello          # Linux/macOS
hello.exe        # Windows
```

Resultado:
```
Olá, PyxCore!
```

## Variáveis e Funções

### Crie `math_demo.pyx`

```pyx
// Função com anotações de tipo
fn add(a: int, b: int) -> int {
    ret a + b
}

fn factorial(n: int) -> int {
    if n <= 1 {
        ret 1
    } else {
        ret n * factorial(n - 1)
    }
}

fn main() {
    let x = 10          // Tipo inferido como int
    let y = 20
    let sum = add(x, y)
    
    print("Soma: ")
    print(sum)
    print("\n")
    
    let fact_5 = factorial(5)
    print("5! = ")
    print(fact_5)
}
```

Compile e execute:
```bash
pyxc math_demo.pyx -o math_demo
./math_demo
```

## Trabalhando com Coleções

### Crie `collections_demo.pyx`

```pyx
fn main() {
    // Listas
    let nums = [1, 2, 3, 4, 5]
    print("Primeiro elemento: ")
    print(nums[0])
    
    // Mapas
    let ages = map<str, int>()
    ages.set("Alice", 30)
    ages.set("Bob", 25)
    
    // Iteração com range
    for i in range(1, 4) {
        print(i)
        print(" ")
    }
}
```

## Correspondência de Padrões

### Crie `pattern_demo.pyx`

```pyx
fn describe(val: int) {
    match val {
        0          => print("zero")
        1          => print("um")
        2..10      => print("dois a dez")
        n if n > 100 => print("número grande")
        _          => print("outro")
    }
}

fn main() {
    describe(5)     // Resultado: dois a dez
    print("\n")
    describe(200)   // Resultado: número grande
}
```

## Trabalhando com Classes

### Crie `class_demo.pyx`

```pyx
class Person {
    pub let name: str
    pub let age: int
    
    fn init(name: str, age: int) {
        self.name = name
        self.age = age
    }
    
    pub fn introduce() {
        print("Olá, eu sou ")
        print(self.name)
        print(" e tenho ")
        print(self.age)
        print(" anos")
    }
    
    pub fn is_adult() -> bool {
        ret self.age >= 18
    }
}

fn main() {
    let person = Person("Alice", 30)
    person.introduce()
    print("\n")
    
    if person.is_adult() {
        print("Maior de idade: sim")
    } else {
        print("Maior de idade: não")
    }
}
```

## Tratamento de Erros

### Crie `error_demo.pyx`

```pyx
fn divide(a: float, b: float) -> result<float, str> {
    if b == 0.0 {
        ret Err("Não é possível dividir por zero")
    }
    ret Ok(a / b)
}

fn main() {
    match divide(10.0, 2.0) {
        Ok(result) => {
            print("Resultado: ")
            print(result)
        }
        Err(msg) => {
            print("Erro: ")
            print(msg)
        }
    }
    
    print("\n")
    
    match divide(10.0, 0.0) {
        Ok(result) => {
            print("Resultado: ")
            print(result)
        }
        Err(msg) => {
            print("Erro: ")
            print(msg)
        }
    }
}
```

## Using the REPL

Interactive REPL for quick experimentation:

```bash
python pyx.py --repl
```

If you are on Windows, use:

```bash
pyx.bat --repl
```

```
pyx> let x = 42
pyx> print(x)
42
pyx> exit
```

## Tips & Tricks

### 1. Type Checking Without Compiling

```bash
python pyx.py myfile.pyx --check-only
```

### 2. View Generated C Code

```bash
# Look in current directory
ls *.c

# View C code
cat myfile.c
```

### 3. Optimization Levels

```bash
python pyx.py myfile.pyx -O0  # No optimization (debug)
python pyx.py myfile.pyx -O2  # Recommended
python pyx.py myfile.pyx -O3  # Maximum optimization
```

## Common Errors

### "Type mismatch: expected X, got Y"

```pyx
// ❌ Wrong
let x: int = "hello"  // Error: str cannot be assigned to int

// ✅ Correct
let x: str = "hello"
let y: int = 42
```

### "Undefined symbol: X"

```pyx
// ❌ Wrong
print(undefined_var)  // Error: undefined_var not defined

// ✅ Correct
let my_var = 42
print(my_var)
```

### "Syntax error"

```pyx
// ❌ Wrong (missing type)
fn add(a, b) { ret a + b }

// ✅ Correct
fn add(a: int, b: int) -> int { ret a + b }
```

## Next Steps

1.
2. **Explore Examples**: See [examples/](examples/) for more code samples
3. **Standard Library**: Learn about [STDLIB.md](STDLIB.md)
4. **Join the Community**: Discuss ideas on Discord or GitHub

## Resources


- 📖 **Standard Library**: [STDLIB.md](STDLIB.md)
- 💡 **Examples**: [examples/](examples/)
- 🐛 **Report Issues**: https://github.com/lipeedeveloper/pyxcore/issues
- 💬 **Discussions**: https://github.com/lipeedeveloper/pyxcore/discussions

---

Happy coding! 🚀
