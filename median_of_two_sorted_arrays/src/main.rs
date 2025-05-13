fn main() {
    let arr_1 = vec![1,3];
    let arr_2 = vec![3];
    Solution::find_median_sorted_arrays(arr_1, arr_2);

}


struct Solution {}

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) {
        println!("{:?} {:?}", nums1, nums2)
    }
}



/*
nums1[i - 1] <= nums2[j]     # lewa część nums1 <= prawa część nums2
nums2[j - 1] <= nums1[i]     # lewa część nums2 <= prawa część nums1

✅ Twoim celem jest:
Znalezienie takiego podziału tablic nums1 i nums2, aby:

wszystkie elementy po lewej stronie podziału były mniejsze lub równe tym po prawej,

a łączna liczba elementów po lewej stronie była równa połowie długości obu tablic (lub połowa + 1 dla nieparzystej liczby elementów).


*/
