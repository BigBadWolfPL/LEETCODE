
fn main() {
    let mut case_1 = vec![3,2,2,3];
    println!("i: {}", Solution::remove_element(&mut case_1, 3));
}

struct Solution {}

impl Solution {
    fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut i = 0;
        for idx in 0..nums.len() {
            if nums[idx] != val {
                nums[i] = nums[idx];
                i += 1;
            }
        }
        i as i32
    }
}
