use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn simple_benchmark(c: &mut Criterion) {
    c.bench_function("simple_benchmark", |b| {
        b.iter(|| {
            black_box(1 + 1);  // bardzo prosty test
        })
    });
}

fn repeat_solution(nums: &Vec<i32>) -> Vec<i32> {
    nums.repeat(2)
}

fn extend_solution(nums: &Vec<i32>) -> Vec<i32> {
    let mut result = Vec::with_capacity(nums.len() * 2);
    result.extend_from_slice(nums);
    result.extend_from_slice(nums);
    result
}

fn bench_concat(c: &mut Criterion) {
    let nums: Vec<i32> = (0..100_000).collect(); // testowy wektor

    c.bench_function("repeat_solution", |b| {
        b.iter(|| repeat_solution(black_box(&nums)))
    });

    c.bench_function("extend_solution", |b| {
        b.iter(|| extend_solution(black_box(&nums)))
    });
}

criterion_group!(benches, simple_benchmark, bench_concat);  // dodajemy oba benchmarki
criterion_main!(benches);
