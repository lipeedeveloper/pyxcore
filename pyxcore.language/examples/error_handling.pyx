// PyxCore Example 5: Error Handling with Result

fn divide(a: float, b: float) -> result<float, str> {
    if b == 0.0 {
        ret Err("Division by zero")
    }
    ret Ok(a / b)
}

fn safe_divide(a: float, b: float) -> float {
    match divide(a, b) {
        Ok(result) => ret result
        Err(msg)   => {
            print("Error: ")
            print(msg)
            ret 0.0
        }
    }
}

fn main() {
    let result1 = safe_divide(10.0, 2.0)
    print("10 / 2 = ")
    print(result1)
    
    let result2 = safe_divide(10.0, 0.0)
    print("10 / 0 = ")
    print(result2)
}
