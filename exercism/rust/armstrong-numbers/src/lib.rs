fn length(num: u32, count: u32) -> u32 {
    if num < 10 {
        return count + 1
    }
   length(num % 10, count + 1) 
}
pub fn is_armstrong_number(num: u32) -> bool {
    let len = length(num, 0);
    let result: u32 = num.to_string().chars()
    .map(|x| x.to_digit(10).unwrap().pow(len))
    .sum();
    result == num
}
