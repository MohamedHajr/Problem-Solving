//pub fn raindrops(n: u32) -> String {
//    match (n % 3, n % 5, n % 7) {
//        (0, 0, 0) => "PlingPlangPlong".to_string(),
//        (0, _, 0) => "PlingPlong".to_string(),
//        (_, 0, 0) => "PlangPlong".to_string(),
//        (0, 0, _) => "PlingPlang".to_string(),
//        (0, _, _) => "Pling".to_string(),
//        (_, 0, _) => "Plang".to_string(),
//        (_, _, 0) => "Plong".to_string(),
//        (_, _, _) => n.to_string()
//    }
//}

const WORDS: [(usize, &'static str); 3] = [
    (3, "Pling"),
    (5, "Plang"),
    (7, "Plong")
];

pub fn raindrops(n: usize) -> String {
    match WORDS.iter().filter(|&&(d, _)| n % d == 0).map(|&(_, w)| w).collect::<String>() {
        ref res if !res.is_empty() => res.to_owned(),
        _                          => n.to_string()
    }
}
