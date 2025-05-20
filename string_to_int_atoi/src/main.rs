fn main() {

}

struct Solution {}

impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let mut result = String::new();
        let temp = s.trim();
        let mut zero = true;

        for ch in temp.chars() {
            if result.is_empty() && ch == '-' {
                result.push(ch);
            } else if ch.is_ascii_digit() {
                result.push(ch);
                if ch != '0' {
                    zero = false;
                }
            } else if result.is_empty() && ch == '+' {
                result.push(ch);
            } else {
                break;
            }
        }
        let final_result = result.parse::<i64>().unwrap_or(0);
        if !result.is_empty() && final_result == 0 {
            if zero {
                return 0;
            } else {
                if result.starts_with("-") {
                    return i32::MIN;
                } else {
                    return i32::MAX;
                }
            }
        }
        if final_result > i32::MAX as i64{
            return i32::MAX;
        } else if final_result < i32::MIN as i64 {
            return  i32::MIN;
        }
        final_result as i32
    }
}



#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_basic_positive() {
        assert_eq!(Solution::my_atoi("42".to_string()), 42);
    }

    #[test]
    fn test_with_spaces() {
        assert_eq!(Solution::my_atoi("   -42".to_string()), -42);
    }

    #[test]
    fn test_with_text_after_number() {
        assert_eq!(Solution::my_atoi("4193 with words".to_string()), 4193);
    }

    #[test]
    fn test_text_before_number() {
        assert_eq!(Solution::my_atoi("words and 987".to_string()), 0);
    }

    #[test]
    fn test_overflow_positive() {
        assert_eq!(Solution::my_atoi("91283472332".to_string()), i32::MAX);
    }

    #[test]
    fn test_overflow_negative() {
        assert_eq!(Solution::my_atoi("-91283472332".to_string()), i32::MIN);
    }

    #[test]
    fn test_only_plus_or_minus() {
        assert_eq!(Solution::my_atoi("+".to_string()), 0);
        assert_eq!(Solution::my_atoi("-".to_string()), 0);
    }

    #[test]
    fn test_multiple_signs() {
        assert_eq!(Solution::my_atoi("++1".to_string()), 0);
        assert_eq!(Solution::my_atoi("--1".to_string()), 0);
        assert_eq!(Solution::my_atoi("+-2".to_string()), 0);
    }

    #[test]
    fn test_leading_zeros_and_plus() {
        assert_eq!(Solution::my_atoi("+0214+748f364239".to_string()), 214);
        assert_eq!(Solution::my_atoi("-214+748f364239".to_string()), -214);
        assert_eq!(Solution::my_atoi("0+0214+748f364239".to_string()), 0);
    }

    #[test]
    fn test_with_weird_characters() {
        assert_eq!(Solution::my_atoi("  -0012a42".to_string()), -12);
    }

    #[test]
    fn test_empty_and_whitespace_only() {
        assert_eq!(Solution::my_atoi("".to_string()), 0);
        assert_eq!(Solution::my_atoi("   ".to_string()), 0);
    }

    #[test]
    fn test_plus_minus() {
        assert_eq!(Solution::my_atoi("-+12".to_string()), 0);
    }
    #[test]
    fn test_edge_values() {
        assert_eq!(Solution::my_atoi("2147483647".to_string()), 2147483647);
        assert_eq!(Solution::my_atoi("-2147483648".to_string()), -2147483648);
    }
    #[test]
    fn test_long_number_with_leading_zeros() {
        assert_eq!(Solution::my_atoi("000000000000000000000000001234".to_string()), 1234);
    }
    #[test]
    fn test_long_number_zeros() {
        assert_eq!(Solution::my_atoi("20000000000000000000".to_string()), 2147483647);
    }
    #[test]
    fn test_large_number() {
        assert_eq!(Solution::my_atoi("1234567890123456789012345678901234567890".to_string()), 2147483647);
    }
    #[test]
    fn negative_test_large_number() {
        assert_eq!(Solution::my_atoi("-1234567890123456789012345678901234567890".to_string()), -2147483648);
    }
}