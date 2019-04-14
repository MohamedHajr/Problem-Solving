#[macro_use] extern crate itertools;

fn main(){
    println!("{}", checkPermutation("abb".to_string(), "bba".to_string()))
}

fn checkPermutation(&s1: String, &s2: String) -> bool{
        let bit_vector: u32 = 0;
        for (x, y) in izip!(&s1, &s2) {
            const mask1: u32 = 1 << x as u32;
            const mask2: u32 = 1 << y as u32;     
            bit_vector ^= mask1;
            bit_vector ^= mask2;
        }
        if bit_vector > 0 {
            return false
        }
        true
}

