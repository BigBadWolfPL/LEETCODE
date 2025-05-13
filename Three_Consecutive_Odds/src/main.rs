fn main() {

    let test_1 = vec![1,2,34,3,4,5,7,23,12];

    println!("RESULT = {}", Solution::three_consecutive_odds(test_1));
}

struct Solution {}

impl Solution {
    pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
        let mut counter = 0;
        for num in arr {
            if num % 2 != 0 {
                counter += 1;
                if counter == 3 {
                    return true;
                }
            } else {
                counter = 0;
            }
        }
        false
    }
}

/*
struct Solution {}

impl Solution {
    pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
        let mut counter = 0;
        for num in arr {
            if num % 2 != 0 {
                counter += 1;
                if counter == 3 {
                    return true;
                }
            } else {
                counter = 0;
            }
        }
        false
    }
}
*/