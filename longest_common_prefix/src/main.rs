fn main() {
    let test_1 = vec![
        "flower".to_string(),
        "flow".to_string(),
        "flight".to_string(),
    ];
    println!("WYNIK: {}", Solution::longest_common_prefix(test_1));
}

struct Solution {}

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
            return "".into();
        }
        let first = strs[0].as_bytes();
        let min_length = strs.iter().map(|w| w.len()).min().unwrap_or(0);

        for idx in 0..min_length {
            for word in strs.iter() {
                if first[idx] != word.as_bytes()[idx] {
                    return String::from_utf8_lossy(&first[..idx]).into();
                }
            }
        }
        String::from_utf8_lossy(&first[..min_length]).into()
    }
}

/*
fn main() {
    let test_1 = vec![
        "flower".to_string(),
        "flow".to_string(),
        "flight".to_string(),
    ];
    println!("WYNIK: {}", Solution::longest_common_prefix(test_1));
}

struct Solution {}

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.len() == 0 {
            return "".into();
        }
        let strs_chars: Vec<Vec<char>> = strs
            .iter()
            .map(|x| x.chars().collect::<Vec<char>>())
            .collect();

        let min_length = strs_chars.iter().map(|x| x.len()).min().unwrap_or(0);

        for idx in 0..min_length {
            for word in &strs_chars {
                if strs_chars[0][idx] != word[idx] {
                    return strs_chars[0][..idx].iter().collect();
                }
            }
        }
        strs_chars[0][..min_length].iter().collect()
    }
}
*/
