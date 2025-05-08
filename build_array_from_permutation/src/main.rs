
fn main() {
    let data = vec![0,2,1,5,3,4];
    let ans = Solution::build_array(data);
    println!("{:?}", ans);
}


struct Solution {}

impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans: Vec<i32> = Vec::with_capacity(nums.len());
        for i in 0..nums.len() {
            let idx = nums[i] as usize;
            ans.push(nums[idx]);
        }
        ans
    }
}



/*
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]



impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans: Vec<i32> = Vec::new();
        for i in 0..nums.len() {
            let idx = nums[i] as usize;
            ans.push(nums[idx]);
        }
        ans
    }
}


    impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        nums.iter().map(|&i| nums[i as usize]).collect()
    }
}

*/