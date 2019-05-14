fn push(mut vec: Vec<u64>, n: u64) -> Vec<u64> {
   vec.push(n); 
   vec
}
pub fn factors(n: u64) -> Vec<u64> {
    fn go(current: u64, factor: u64, factors: Vec<u64>) -> Vec<u64> {
        match current  {
            1 => factors,
            _n if _n % factor == 0 => go(current / factor, factor,  push(factors, factor)),
            _ => go(current, factor + 1, factors)
        }
    }
    go(n, 2, Vec::new())
}
