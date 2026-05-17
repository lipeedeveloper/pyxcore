%YAML 1.2
---
# PyxCore v2.0 - Quick Reference Card

title: PyxCore Language Quick Reference
version: 2.0

# ============================================================================
# TYPES
# ============================================================================

types:
  primitives:
    - "int        # 64-bit signed integer"
    - "uint       # 64-bit unsigned integer"
    - "float      # 64-bit double precision"
    - "bool       # true | false"
    - "char       # UTF-8 character 'a'"
    - "str        # immutable UTF-8 string"
    - "byte       # raw 8-bit unsigned"
  
  composite:
    - "list<T>         # dynamic array"
    - "map<K, V>       # hash map"
    - "set<T>          # hash set"
    - "tuple<A, B>     # immutable tuple"
    - "option<T>       # Some(v) | None"
    - "result<T, E>    # Ok(v) | Err(e)"
  
  special:
    - "null      # explicit null"
    - "never     # never returns"
    - "any       # disable type checking"

# ============================================================================
# VARIABLES
# ============================================================================

variables:
  immutable: |
    let x = 42          # Type inferred
    let name: str = "Ada"
    
  constant: |
    const PI: float = 3.14159
    
  destructuring: |
    let (a, b) = (1, 2)
    let [head, ...tail] = [1, 2, 3]

# ============================================================================
# FUNCTIONS
# ============================================================================

functions:
  basic: |
    fn add(a: int, b: int) -> int {
        ret a + b
    }
  
  default_params: |
    fn greet(name: str, greeting: str = "Hello") -> str {
        ret greeting + ", " + name + "!"
    }
  
  variadic: |
    fn sum(...nums: int) -> int {
        let total = 0
        for n in nums { total += n }
        ret total
    }
  
  closure: |
    let double = fn(x: int) { x * 2 }
    
  higher_order: |
    fn apply(f: fn(int) -> int, v: int) -> int {
        ret f(v)
    }
  
  async: |
    async fn fetch(url: str) -> str {
        let resp = await http.get(url)
        ret resp.body
    }

# ============================================================================
# CONTROL FLOW
# ============================================================================

control_flow:
  if_statement: |
    if x > 0 {
        print("positive")
    } elif x == 0 {
        print("zero")
    } else {
        print("negative")
    }
  
  ternary: |
    let label = if x > 0 { "pos" } else { "neg" }
  
  while_loop: |
    while condition {
        if done { break }
        if skip { continue }
    }
  
  for_loop: |
    for i in range(10) { }              # 0..9
    for i in range(1, 11) { }           # 1..10
    for item in list { }
    for (i, v) in list.enumerate() { }
  
  match_expression: |
    match value {
        0       => print("zero")
        1..10   => print("small")
        n if n > 100 => print("big")
        _       => print("other")
    }

# ============================================================================
# CLASSES & OOP
# ============================================================================

classes:
  basic: |
    class Point {
        pub let x: float
        pub let y: float
        
        fn init(x: float, y: float) {
            self.x = x
            self.y = y
        }
        
        pub fn distance() -> float {
            ret sqrt(x*x + y*y)
        }
    }
  
  inheritance: |
    class Dog extends Animal {
        pub let breed: str
        
        override fn speak() -> str {
            ret self.name + " says Woof!"
        }
    }
  
  interface: |
    interface Drawable {
        fn draw()
        fn resize(factor: float)
    }
  
  implementation: |
    class Circle implements Drawable {
        override fn draw() { }
        override fn resize(f: float) { }
    }

# ============================================================================
# ERROR HANDLING
# ============================================================================

error_handling:
  result_type: |
    fn divide(a: float, b: float) -> result<float, str> {
        if b == 0.0 { ret Err("division by zero") }
        ret Ok(a / b)
    }
  
  handling: |
    match divide(10.0, 2.0) {
        Ok(v)  => print("Result: " + str(v))
        Err(e) => print("Error: " + e)
    }
  
  error_propagation: |
    fn safe_divide(a: str, b: str) -> result<float, str> {
        let x = parse_float(a)?
        let y = parse_float(b)?
        ret divide(x, y)
    }
  
  panic: |
    if invalid { panic("Critical error") }

# ============================================================================
# MEMORY & SAFETY
# ============================================================================

memory:
  ownership: |
    let s = "hello"     # s owns the string
    let t = s           # ownership moved
    let t = s.clone()   # explicit clone
  
  borrowing: |
    fn print_len(s: &str) { print(len(s)) }
    fn append(s: &mut str, c: char) { s.push(c) }
  
  null_safety: |
    let x: str = null       # ERROR - str is non-nullable
    let x: str? = null      # OK - nullable
    let x: option<str>      # explicit optional

# ============================================================================
# STANDARD LIBRARY
# ============================================================================

stdlib:
  io: |
    io.print(...)
    io.println(...)
    io.read_line() -> str
  
  math: |
    math.PI, math.E
    math.sqrt(x) -> float
    math.pow(x, exp) -> float
    math.sin(x), math.cos(x)
  
  string: |
    s.len() -> int
    s.upper() -> str
    s.lower() -> str
    s.split(sep: str) -> list<str>
    s.contains(sub: str) -> bool
  
  list: |
    l.push(v)
    l.pop() -> option<T>
    l.map(fn) -> list<U>
    l.filter(fn) -> list<T>
    l.sort()
  
  map: |
    m.get(k) -> option<V>
    m.set(k, v)
    m.keys() -> list<K>
    m.values() -> list<V>

# ============================================================================
# OPERATORS
# ============================================================================

operators:
  arithmetic:
    - "+   # Addition"
    - "-   # Subtraction"
    - "*   # Multiplication"
    - "/   # Division"
    - "%   # Modulo"
  
  comparison:
    - "==  # Equal"
    - "!=  # Not equal"
    - "<   # Less than"
    - ">   # Greater than"
    - "<=  # Less than or equal"
    - ">=  # Greater than or equal"
  
  logical:
    - "&&  # Logical AND"
    - "||  # Logical OR"
    - "!   # Logical NOT"
  
  bitwise:
    - "&   # Bitwise AND"
    - "|   # Bitwise OR"
    - "^   # Bitwise XOR"
    - "~   # Bitwise NOT"
    - "<<  # Left shift"
    - ">>  # Right shift"
  
  assignment:
    - "=   # Assignment"
    - "+=  # Add assign"
    - "-=  # Subtract assign"
    - "*=  # Multiply assign"
    - "/=  # Divide assign"
  
  special:
    - "..   # Exclusive range"
    - "..=  # Inclusive range"
    - "?    # Try/unwrap"
    - "??   # Null coalesce"
    - "=>   # Match arm"
    - "->   # Function return"
    - "|>   # Pipe operator"

# ============================================================================
# DATABASE API
# ============================================================================

database:
  basics: |
    let db = db_connect("app")
    let coll = db_create_collection(db, "users")
    db_insert(coll, "user:1", "Alice")
    let value = db_find(coll, "user:1")
    db_update(coll, "user:1", "Alicia")
    db_delete(coll, "user:1")
    let count = db_count(coll)
    db_close(db)

  query: |
    let match = db_query(coll, "user:2")
    if match != null {
        print(match)
    }

  notes: |
    - `db_connect(name)` cria um banco de dados em memória.
    - `db_create_collection(db, name)` cria ou retorna uma coleção.
    - `db_insert(coll, key, value)` insere ou atualiza um valor.
    - `db_find(coll, key)` retorna valor por chave.
    - `db_update(coll, key, value)` atualiza um valor existente.
    - `db_delete(coll, key)` remove um item.
    - `db_count(coll)` retorna o total de itens.

# ============================================================================
# KEYWORDS (Reserved)
# ============================================================================

keywords:
  control: "if elif else while for in loop break continue"
  definitions: "let const fn ret class interface type enum"
  modifiers: "pub priv static abstract override async await"
  special: "match self super import export defer panic assert"

# ============================================================================
# SYNTAX PATTERNS
# ============================================================================

patterns:
  string_interpolation: |
    let name = "Ada"
    let msg = f"Hello, {name}! Age: {age + 5}"
  
  pipe_operator: |
    let result = data
        |> filter(fn(x) { x > 0 })
        |> map(fn(x) { x * 2 })
        |> reduce(0, fn(a, x) { a + x })
  
  optional_chaining: |
    let name = user?.profile?.name ?? "anonymous"
  
  with_statement: |
    with file = fs.open("data.txt") {
        print(file.read())
    }  # auto-closed
  
  defer_statement: |
    fn open_conn() {
        let conn = db.connect()
        defer conn.close()  # always runs
        do_work(conn)
    }

# ============================================================================
# COMPILER COMMANDS
# ============================================================================

compiler:
  basic: |
    pyxc main.pyx           # Compile
    pyxc main.pyx -o app    # Output file
    pyxc main.pyx --check-only  # Type check
  
  optimization: |
    pyxc main.pyx -O0   # Debug (no optimization)
    pyxc main.pyx -O2   # Default
    pyxc main.pyx -O3   # Maximum
  
  targets: |
    pyxc main.pyx --target native    # x86-64 (default)
    pyxc main.pyx --target wasm32    # WebAssembly
    pyxc main.pyx --target arm64     # ARM 64-bit
  
  features: |
    pyxc main.pyx --gc                  # Enable GC
    pyxc main.pyx --emit-ir             # Emit IR
    pyxc main.pyx --emit-asm            # Emit ASM
  
  repl: |
    pyx                 # Interactive REPL

...
