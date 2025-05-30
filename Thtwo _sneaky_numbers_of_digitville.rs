use std::collections::HashMap;

fn main() {
    let result = Solution::get_sneaky_numbers(vec![0, 3, 2, 1, 3, 2]);
    println!("Wrong output: {:?}", result);
}

struct Solution {}

impl Solution {
    pub fn get_sneaky_numbers(nums: Vec<i32>) -> Vec<i32> {
        let mut result: HashMap<i32, i32> = HashMap::with_capacity(nums.len());
        for num in nums {
            result.entry(num).and_modify(|c| *c += 1).or_insert(1);
        }
        result
            .iter()
            .filter_map(|(&k, &v)| if v >= 2 { Some(k) } else { None })
            .collect()
    }
}

/*
impl Solution {
    pub fn get_sneaky_numbers(nums: Vec<i32>) -> Vec<i32> {
        let mut result: HashMap<i32, i32> = HashMap::with_capacity(nums.len());
        for num in nums {
            result.entry(num).and_modify(|c| *c += 1).or_insert(1);
        }
        result.iter()
            .filter(|(&_, &v)| v >= 2)
            .map(|(&k, &_)| k)
            .collect::<Vec<i32>>()
    }
}

*/
