fn main() {
    println!("Wynik: {}", Solution::the_maximum_achievable_x(4, 1));
}


struct Solution {}

impl Solution {
    pub fn the_maximum_achievable_x(num: i32, t: i32) -> i32 {
        num + 2 * t
    }
}

/*
Treść zadania:
Masz dane dwie liczby całkowite: num oraz t.

Liczba całkowita x jest nazywana osiągalną, jeśli można ją przekształcić w num poprzez wykonanie maksymalnie t razy następującej operacji:

Zwiększ lub zmniejsz x o 1, a jednocześnie wykonaj przeciwną operację na num (jeśli zwiększysz x, to zmniejsz num, i odwrotnie).

Zwróć największą możliwą wartość x, która jest osiągalna w ten sposób.

Gwarantuje się, że istnieje co najmniej jedna taka liczba x.
*/