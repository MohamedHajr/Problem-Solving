//https://users.rust-lang.org/t/reading-and-parsing-a-line-from-stdin-containing-3-integers/7265
use std::io;
use std::io::prelude::*;

fn main () {
        let reader = io::stdin();
        let num: u32 = reader
        .lock()
        .lines()
        .next()
        .unwrap()
        .ok()
        .unwrap()
        .trim()
        .parse()
        .unwrap();
        let mut a_str = String::new();
        reader.read_line(&mut a_str).expect("read error");
        let mut vec = a_str.split_whitespace()
            .map(|x| x.parse::<i32>().expect("parse error"))
            .collect::<Vec<i32>>();
       println!("{}", getUnique(vec));
}

fn getUnique(array: Vec<i32>) -> i32 {
    let mut store: i32 = 0;
    for num in array {
        store ^= num;
    }
    return store
}
