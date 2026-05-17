// PyxCore Example 3: Classes and OOP

class Point {
    pub let x: float
    pub let y: float
    
    fn init(x: float, y: float) {
        self.x = x
        self.y = y
    }
    
    pub fn distance() -> float {
        ret sqrt(self.x * self.x + self.y * self.y)
    }
    
    pub fn display() {
        print("Point(")
        print(self.x)
        print(", ")
        print(self.y)
        print(")")
    }
}

fn main() {
    let p = Point(3.0, 4.0)
    p.display()
    print(" Distance: ")
    print(p.distance())
}
