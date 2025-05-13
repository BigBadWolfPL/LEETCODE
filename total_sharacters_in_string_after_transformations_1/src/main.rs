fn main() {
    println!("WYNIK: {}", Solution::length_after_transformations("abcyy".to_string(), 2)); // 7
}


struct Solution {}

impl Solution {
    pub fn length_after_transformations(s: String, t: i32) -> i32 {
        let mut result = s;
        for _ in 0..t {
        result = result
            .replace("z", "ab")
            .replace("y", "z")
            .replace("x", "y")
            .replace("w", "x")
            .replace("v", "w")
            .replace("u", "v")
            .replace("t", "u")
            .replace("s", "t")
            .replace("r", "s")
            .replace("q", "r")
            .replace("p", "q")
            .replace("o", "p")
            .replace("n", "o")
            .replace("m", "n")
            .replace("l", "m")
            .replace("k", "l")
            .replace("j", "k")
            .replace("i", "j")
            .replace("h", "i")
            .replace("g", "h")
            .replace("f", "g")
            .replace("e", "f")
            .replace("d", "e")
            .replace("c", "d")
            .replace("b", "c")
            .replace("a", "b");
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