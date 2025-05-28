use std::collections::HashMap;


fn main() {
    let result = Solution::appeal_sum("abbca".to_string());
    assert!(result == 28, "Wrong output {}", result);
}


struct Solution {}

impl Solution {
    pub fn appeal_sum(s: String) -> i64 {
        let mut characters: HashMap<char, i64> = HashMap::new();
        let mut result: i64 = 0;
        let mut current: i64 = 0;
        for (idx, ch) in s.chars().enumerate() {
            let prev_index = *characters.get(&ch).unwrap_or(&-1);
            current += idx as i64 - prev_index;
            result += current;
            characters.insert(ch, idx as i64);
        }
        result
    }
}
