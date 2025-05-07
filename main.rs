use std::collections::HashMap;

fn main() {
    let test_1 = "XIV".to_string(); // 14
    let test_2 = "MCMXCIV".to_string(); // 1994
    let test_3 = "LVIII".to_string(); // 58
    let test_4 = "III".to_string(); // 3
    let test_5 = "MCDLXXVI".to_string(); // 1476
    println!("{}", roman_to_int(test_1));
    println!("{}", roman_to_int(test_2));
    println!("{}", roman_to_int(test_3));
    println!("{}", roman_to_int(test_4));

    println!("INNE PODEJŚCIE = {}", inne_podejscie(test_5));

    let a = [1, 2, 3];

    // the sum of all of the elements of the array
    let sum = a.iter().fold(0, |acc, x| acc + x);

    assert_eq!(sum, 6);
}

pub fn roman_to_int(s: String) -> i32 {
    let roman_values = HashMap::from([
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000),
    ]);
    let mut result = 0;
    let mut previous = 0;

    for c in s.chars().rev() {
        let value = *roman_values.get(&c).unwrap_or(&0);
        if value < previous {
            result -= value;
        } else {
            result += value;
        }
        previous = value;
    }
    result
}

pub fn inne_podejscie(s: String) -> i32 {
    let roman_values = HashMap::from([
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000),
    ]);
    s.chars().rev().fold((0, 0), |(mut result, previous), c| {
        let value = *roman_values.get(&c).unwrap_or(&0);
        if value < previous {
            result -= value;
        } else {
            result += value;
        }
        (result, value) // WYTŁUMACZ TĘ LINIĘ KODU
    })
    .0
}
/*
W tej funkcji:

fold((0, 0), |(mut result, previous), c| {...}) zaczyna z początkową krotką (0, 0).

W każdej iteracji:

Przetwarzamy symbol rzymski, porównujemy go z poprzednim, modyfikujemy result, i zwracamy nowy stan (result, value).

Po zakończeniu fold() wyciągamy result (pierwszy element krotki) za pomocą .0.
*/