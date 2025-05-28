use std::collections::HashMap;


fn main() {
    let result = Solution::appeal_sum("abbca".to_string());
    assert!(result == 28, "Wrong output {}", result);
}


struct Solution {}

impl Solution {
    pub fn appeal_sum(s: String) -> i32 {
        let mut characters: HashMap<char, i32> = HashMap::new();
        let mut result = 0;
        let mut current = 0;
        for (idx, ch) in s.chars().enumerate() {
            let prev_index = characters.get(&ch).unwrap_or(&-1);
            current += idx as i32 - prev_index;
            result += current;
            characters.entry(ch).and_modify(|x| *x = idx as i32).or_insert(idx as i32);
        }
        result
    }
}