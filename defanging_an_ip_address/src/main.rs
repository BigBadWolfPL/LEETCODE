fn main() {
    let test_1 = "255.100.50.0".to_string(); // "255[.]100[.]50[.]0"
    let test_2 = "1.1.1.1".to_string(); // "1[.]1[.]1[.]1"
    println!("{}", Solution::defang_i_paddr(test_1));
    println!("{}", Solution::defang_i_paddr(test_2));
}

struct Solution {}

impl Solution {
    pub fn defang_i_paddr(address: String) -> String {
        address.replace(".", "[.]")
    }
}