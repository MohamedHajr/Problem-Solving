fn is_prime(n: u32) -> bool {
    let upper_limit = (n as f64).sqrt() as u32 + 1;
    !(2..upper_limit).any(|number| n % number == 0)
}


pub fn nth(n: u32) -> u32 {
    match n {
        0 => 2,
        _ => (1..).step_by(2).filter(|x| is_prime(*x)).nth(n as usize).unwrap()
    }
}

