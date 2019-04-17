use std::cmp;

fn main(){
    let seq = get_alternating_sequence(0b11011101111);
    println!("{:?}", find_longest_sequence(seq)) 
}

fn get_alternating_sequence(mut number: u32) -> Vec<u32>{
    let mut result : Vec<u32> = Vec::new();
    let mut curr = 0;
    let mut counter = 0;
    for _i in 0..32{
        if (number & 1) != curr {
                result.push(counter);
                curr = number & 1;
                counter = 0;
        } 
        counter += 1;
        number >>= 1;
    }
    result.push(counter);
    result
}

fn find_longest_sequence(seq: Vec<u32>) -> u32 {
    let mut max_seq = 1;
    for i in (0..seq.len()).step_by(2) {
        let zero_seq = seq[i];
        let left_side = if i - 1 >= 0 {
            seq[i-1]
        } else {
            0
        };    
        let right_side = if i + 1 <= seq.len() {
            seq[i+1]
        } else {
            0
        };

        let mut this_seq = 0;
        if zero_seq == 1 {
            this_seq = left_side + 1 + right_side;
        } else if zero_seq > 1 {
            this_seq = 1 + cmp::max(left_side, right_side)
        } else if zero_seq == 0 {
            this_seq = cmp::max(left_side, right_side)
        }
        max_seq = cmp::max(max_seq, this_seq)
    }
   max_seq             
}
