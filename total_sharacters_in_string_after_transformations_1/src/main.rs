fn main() {
    println!("{}", Solution::length_after_transformations("abcyy".to_string(), 2)); // 7
}


struct Solution {}

impl Solution {
    pub fn length_after_transformations(s: String, t: i32) -> i32 {
        let mut result = s;
        for _ in 0..t {
            result = result.replace("z", "ab");
            result = result.replace("y", "z");
        }
        result.len() as i32
    }
}



/*
a => ab (26 operacji)              pozostało 
policzyć lie razy zmieści się 26 w 200




You are given a string s and an integer t, representing the number of transformations to perform. 
In one transformation, every character in s is replaced according to the following rules:

- 'z' with the string "ab".
- Otherwise, replace it with the next character in the alphabet.
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.
*/