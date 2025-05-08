use std::cmp::Ordering;

fn main() {
    let test_1 = vec![9,12,5,10,14,3,10];
    let test_2 = vec![-3,4,3,2];
    let res_1 = Solution::pivot_array(test_1, 10);
    let res_2 = Solution::pivot_array(test_2, 2);
    println!("{:?}", res_1);
    println!("{:?}", res_2);
}

struct Solution {}

impl Solution {
    pub fn pivot_array(nums: Vec<i32>, pivot: i32) -> Vec<i32> {
        let mut less: Vec<i32> = Vec::with_capacity(nums.len());
        let mut equal: Vec<i32> = Vec::with_capacity(nums.len());
        let mut greater: Vec<i32> = Vec::with_capacity(nums.len());
        for num in nums {
            match num.cmp(&pivot) {
                Ordering::Less => less.push(num),
                Ordering::Equal => equal.push(num),
                Ordering::Greater => greater.push(num),
            }
        }
        less.extend(equal);
        less.extend(greater);
        less
    }
}


/*
Example 1:

Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]
Explanation: 
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
Example 2:

Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]
Explanation: 
The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.
*/