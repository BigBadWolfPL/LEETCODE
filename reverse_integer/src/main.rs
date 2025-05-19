fn main() {
    println!("RESULT: {}", Solution::reverse(-123));
}

struct Solution {}

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut result = String::new();
        let temp = x.to_string();

        for &ch in temp.as_bytes().iter().rev() {
            let c = ch as char;
                if c != '-' {
                    result.push(c);
                } else {
                    result.insert(0, c);
                }
        }
        result.parse().unwrap_or(0)
    }
}