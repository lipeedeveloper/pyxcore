// PyxCore Example 4: Pattern Matching

type Shape = Circle | Rect | Triangle

fn area(s: Shape) -> float {
    match s {
        Circle(r)    => 3.14159 * r * r
        Rect(w, h)   => w * h
        Triangle(b, h) => 0.5 * b * h
    }
}

fn main() {
    let circle = Circle(5.0)
    let rect = Rect(4.0, 6.0)
    
    print("Circle area: ")
    print(area(circle))
    print("\nRect area: ")
    print(area(rect))
}
