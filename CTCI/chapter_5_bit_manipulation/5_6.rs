fn main() {
    println!("Conversion steps needed -> {}", conversion(29, 15));
}

fn conversion(n1: i32, n2: i32) -> u16 {
    let mut counter = 0;
    let mut n = n1 ^ n2;
    while n != 0 {
        counter += 1;
        n &= n - 1 
    }
    counter
}

