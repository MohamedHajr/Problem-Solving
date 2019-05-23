pub fn brackets_are_balanced(string: &str) -> bool {
    let mut stack: Vec<char> = vec![];
    
    for x in string.chars() {
        match x {
            '{' | '[' | '(' => stack.push(x),
            '}' => if stack.is_empty() || stack.pop() != Some('{') { return false },
            ']' => if stack.is_empty() || stack.pop() != Some('[') { return false },
            ')' => if stack.is_empty() || stack.pop() != Some('(') { return false },
             _  => continue,
        }
    }
    stack.len() == 0 
}
