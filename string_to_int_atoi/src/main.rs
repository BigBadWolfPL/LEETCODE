fn main() {
    println!("RESULT: {}", Solution::my_atoi("-214748364239".to_string())); // 2147483648
}

struct Solution {}

impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let mut result = String::new();
        let temp = s.trim();
        let mut flag_minus = true;

        for ch in temp.chars() {
            if flag_minus && ch == '-' {
                if result.is_empty() {
                    flag_minus = false;
                } else {
                    break;
                }
            } else if ch.is_ascii_digit() {
                result.push(ch);
            } else {
                break;
            }
        }
        let mut final_result = result.parse::<i64>().unwrap_or(0);
        if !flag_minus {
            final_result = -final_result;
        }
        
        if final_result > i32::MAX as i64{
            return i32::MAX;
        } else if final_result < i32::MIN as i64 {
            return  i32::MIN;
        }
        final_result as i32
    }
}