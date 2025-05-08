use std::time::Instant;

fn repeat_solution(nums: &Vec<i32>) -> Vec<i32> {
    nums.repeat(2)
}

fn extend_solution(nums: &Vec<i32>) -> Vec<i32> {
    let n = nums.len();
    let mut result = Vec::with_capacity(n * 2);
    result.extend_from_slice(nums);
    result.extend_from_slice(nums);
    result
}

fn main() {
    let nums: Vec<i32> = (1_000_000_000..1_000_000_000).collect();

    // Benchmark repeat_solution
    let start = Instant::now();
    let result1 = repeat_solution(&nums);
    let duration1 = start.elapsed();
    println!("repeat_solution: {:?} (len: {})", duration1, result1.len());

    // Benchmark extend_solution
    let start = Instant::now();
    let result2 = extend_solution(&nums);
    let duration2 = start.elapsed();
    println!("extend_solution: {:?} (len: {})", duration2, result2.len());
}
