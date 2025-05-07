fn main() {
    let liczba_1 = Solution::score_of_string("zaz".to_string());
    println!("{}", liczba_1);
}

struct Solution {}

impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        let wektor_bajtow = s.into_bytes(); // tworzy ze stringa wektor bajtów
        wektor_bajtow.windows(2).map(|x|x[0].abs_diff(x[1]) as i32).sum() // użycie windows
    }
}

/*
'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50


impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        let bytes = s.into_bytes();
        let first = bytes[0];
        
        bytes[1..].iter().fold((0, first), |(acc, previous), &c| {
        let value = c.abs_diff(previous);
        (acc + value, c)
    }
    ).0 as i32
    }
}

*/
