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
    s.chars()
        .rev()
        .fold((0, 0), |(mut result, previous), c| {
            let value = *roman_values.get(&c).unwrap_or(&0);
            if value < previous {
                result -= value;
            } else {
                result += value;
            }
            (result, value)
        })
        .0
}
/*
W tej funkcji:

fold((0, 0), |(mut result, previous), c| {...}) zaczyna z początkową krotką (0, 0).
W każdej iteracji:
Przetwarzamy symbol rzymski, porównujemy go z poprzednim, modyfikujemy result, i zwracamy nowy stan (result, value). ---> nadpisujemy result przez result i >>>>previous przez value<<<!!!!!!!!!!!!!!
Po zakończeniu fold() wyciągamy result (pierwszy element krotki) za pomocą .0.

!!!!!!!!!!!!!!!!!!!!!!
>>>>>>>>>>>>>>>>>>>>>
Mam jeszcze jedno pytanie do kodu:  "fold((0, 0), |(result, previous), c| .... (result, value) " 
czy krotka na końcu kodu zwracana przez funkcję nadpisuje result przez nowy result a previous przez value?


ChatGPT powiedział:
Tak, dokładnie! W zapisie:


fold((0, 0), |(result, previous), c| {
    ...
    (result, value)
})
każda iteracja fold:
przyjmuje jako argumenty krotkę (result, previous) — czyli wynik i poprzednią wartość z poprzedniej iteracji,
wykonuje ciało lambdy (czyli blok kodu),
zwraca nową krotkę (result, value), która:
ustawia result na nowy wynik po dodaniu/odjęciu wartości,
ustawia previous na bieżącą wartość (value),
ta nowa krotka staje się wejściem do następnej iteracji.
Czyli tak: nowa krotka nadpisuje wartości result i previous na potrzeby kolejnego kroku fold.
Chcesz, żebym to zilustrował na małym przykładzie krok po kroku?



Świetnie! Oto krok po kroku, jak działa fold na przykładzie:

Weźmy prosty przykład: s = "XIV"
Zamienimy string na chars().rev() → iterujemy: 'V', 'I', 'X'
Mapa wartości:

rust
Kopiuj
Edytuj
'I' => 1, 'V' => 5, 'X' => 10
Kod:

rust
Kopiuj
Edytuj
s.chars().rev().fold((0, 0), |(result, previous), c| {
    let value = roman_values[&c];
    if value < previous {
        result -= value;
    } else {
        result += value;
    }
    (result, value)
}).0
Krok po kroku:
1. Start:
result = 0

previous = 0

Iteracja 1: litera 'V'
value = 5

value >= previous (0) → dodajemy: result = 0 + 5 = 5

zwracamy: (5, 5)

Iteracja 2: litera 'I'
previous = 5, result = 5

value = 1

1 < 5 → odejmujemy: result = 5 - 1 = 4

zwracamy: (4, 1)

Iteracja 3: litera 'X'
previous = 1, result = 4

value = 10

10 >= 1 → dodajemy: result = 4 + 10 = 14

zwracamy: (14, 10)

Na końcu:
.0 wybiera 14 z (14, 10), czyli finalny wynik.

>>>>>>>>>>>>>>>>>>>>>>
!!!!!!!!!!!!!!!!!!!!!!!!!


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


*/
