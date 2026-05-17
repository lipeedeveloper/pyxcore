# Standard Library

The PyxCore standard library provides essential functionality organized into modules.

## Module Organization

### io - Input/Output

```pyx
io.print(...)           // Print to stdout
io.println(...)         // Print with newline
io.read_line() -> str   // Read line from stdin
```

### math - Mathematical Functions

```pyx
math.PI, math.E, math.TAU
math.sqrt(x: float) -> float
math.pow(x: float, exp: float) -> float
math.sin(x: float) -> float
math.cos(x: float) -> float
math.abs(x: T) -> T
math.min(a: T, b: T) -> T
math.max(a: T, b: T) -> T
```

### str - String Operations

```pyx
s.len() -> int
s.upper() -> str
s.lower() -> str
s.trim() -> str
s.split(sep: str) -> list<str>
s.contains(sub: str) -> bool
s.starts_with(prefix: str) -> bool
s.replace(old: str, new: str) -> str
```

### list<T> - Dynamic Arrays

```pyx
l.push(v: T)
l.pop() -> option<T>
l.len() -> int
l.contains(v: T) -> bool
l.map(fn: fn(T) -> U) -> list<U>
l.filter(fn: fn(T) -> bool) -> list<T>
l.sort()
l.reverse()
```

### map<K, V> - Hash Maps

```pyx
m.get(k: K) -> option<V>
m.set(k: K, v: V)
m.delete(k: K) -> bool
m.keys() -> list<K>
m.values() -> list<V>
m.entries() -> list<(K, V)>
```

### fs - File System

```pyx
fs.read(path: str) -> result<str, Error>
fs.write(path: str, content: str) -> result<(), Error>
fs.exists(path: str) -> bool
fs.list_dir(path: str) -> result<list<str>, Error>
```

### json - JSON

```pyx
json.encode(v: T) -> str
json.decode<T>(s: str) -> result<T, Error>
```

### time - Time & Dates

```pyx
time.now() -> Timestamp
time.sleep(ms: int)
time.format(ts: Timestamp, fmt: str) -> str
```

### http - HTTP (async)

```pyx
async fn http.get(url: str) -> result<Response, Error>
async fn http.post(url: str, body: str) -> result<Response, Error>
```

## Using Modules

```pyx
import io
import math
import str
import list

fn main() {
    io.print("sqrt(16) = ")
    io.println(math.sqrt(16.0))
}
```

## Creating Custom Modules

```pyx
// File: math/vectors.pyx
pub class Vec2 {
    pub let x: float
    pub let y: float
    
    pub fn length() -> float {
        ret sqrt(x*x + y*y)
    }
}

// Usage in main.pyx
import math.vectors.{Vec2}

fn main() {
    let v = Vec2(3.0, 4.0)
    print(v.length())
}
```

## Extending the Standard Library

To add new functions to the stdlib:

1. Create a `.pyx` file in `stdlib/`
2. Implement functions
3. Add to `stdlib/mod.pyx` (module registry)
4. Rebuild stdlib: `make stdlib`

## Performance Notes

- List operations are O(1) for push/pop (amortized)
- Map operations are O(1) average case
- String operations create new strings (immutable)
- Use iterators for large collections
