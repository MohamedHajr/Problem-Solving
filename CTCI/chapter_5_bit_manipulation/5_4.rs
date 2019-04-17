fn main() {
    let number = 13948;
    let bigger = get_next(number);
    let smaller = get_prev(number);
    println!("{:32b}", bigger);
    println!("{:32b}", smaller);
}
 
fn get_next(number: i32) -> i32{
    let mut n  = number;
    let mut c0 = 0;
    let mut c1 = 0;
    while (n & 1) == 0 && n != 0 {
        c0 += 1;
        n >>= 1;
    }
    while (n & 1) == 1 {
        c1 += 1;
        n >>= 1;
    }
    if c0 + c1 == 31 || c0 + c1 == 0 {
        return -1
    }
    let first_zero = c0 + c1;
    // flip the 0 to 1 
    n = number | (1 << first_zero);
    // clear all bits befor flipped zero
    n &=  !((1 << first_zero) - 1);
    // add the rest of the cleared ones to beggining
    n |= (1 << (c1 - 1)) - 1;
    n 
}

fn get_prev(number: i32) -> i32 {
   let mut n = number; 
   let mut c1 = 0;
   let mut c0 = 0;
   while (n & 1) == 1 {
        c1 += 1;
        n >>= 1;
   }
   if n == 0 {
       return -1
   }
   while (n & 1) == 0 && n != 0 {
       c0 += 1;
       n >>= 1;
   }

   let first_one = c1 + c0;
   // clear the first one bit after a zero + the prev bits 
   n = number & ((!0) << (first_one + 1));
   // add ones before first one bit    
   let mask =  (1 << (c1 + 1)) - 1;
   n |= mask << (c0 - 1);
   n
}
