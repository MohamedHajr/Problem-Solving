fn main() {
    println!("{:32b}", swap_pairs(0b1011011))
} 

fn swap_pairs(num: u32) -> u32 {
    let even = (num << 1) & 0xaaaaaaaa;
    let odd = (num >> 1) & 0x55555555;
    even | odd
}
