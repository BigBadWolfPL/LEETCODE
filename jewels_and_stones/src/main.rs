use std::collections::{HashMap, HashSet};
use std::time::Instant;

fn main() {
    let jewels = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ".repeat(10);
    let stones = "aAAbbbbCcDDeeFfGgHHiiJJkkLLmmNnOopPQQrrSsttUuvvWWxxYyZz".repeat(10_000);

    let now = Instant::now();
    let res1 = Solution1::num_jewels_in_stones(jewels.clone(), stones.clone());
    println!("HashMap: {} in {:?}", res1, now.elapsed());

    let now = Instant::now();
    let res2 = Solution2::num_jewels_in_stones(jewels, stones);
    println!("HashSet: {} in {:?}", res2, now.elapsed());
}

struct Solution1 {}

impl Solution1 {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        let mut counter: HashMap<u8, i32> = HashMap::new();

        for b in stones.as_bytes() {
            counter.entry(*b).and_modify(|c| {*c += 1}).or_insert(1);
        }
        jewels
            .as_bytes()
            .iter()
            .fold(0, |acc, &b| acc + counter.get(&b).unwrap_or(&0))
    }
}

struct Solution2;

impl Solution2 {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        let jewel_set: HashSet<u8> = jewels.bytes().collect();
        stones.bytes().filter(|b| jewel_set.contains(b)).count() as i32
    }
}

