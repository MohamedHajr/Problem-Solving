fn main(){
    println!("0b{:32b}", insert(0b100000000000, 0b10011, 2, 6))
}

fn clear_mask(i: u32, j: u32) -> u32{
    let left_side: u32 = (!0) << j+1;
    let right_side: u32 = (1 << i) - 1;
    return left_side | right_side
}

fn insert(container: u32, m: u32, i: u32, j: u32) -> u32{
    let clearing_mask = clear_mask(i, j);
    let cleared_container = clearing_mask & container;
    return cleared_container |  (m << i)
}

