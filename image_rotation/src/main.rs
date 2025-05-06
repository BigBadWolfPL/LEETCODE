//use std::mem::swap;


fn main() {
    let mut input_data = vec![vec![1,2,3], vec![4,5,6], vec![7,8,9]];
    rotate(&mut input_data);
}


fn rotate(matrix: &mut Vec<Vec<i32>>) {
    let length = matrix.len();
    for i in 0..length {
        for j in i+1..length {
            let temp_1 = matrix[i][j];
            let temp_2 = matrix[j][i];
            matrix[i][j] = temp_2;
            matrix[j][i] = temp_1;
        }
    }
    for row in matrix {
        row.reverse();
    }
}



/*
fn rotate(matrix: &mut Vec<Vec<i32>>) {
    let length = matrix.len();
    for i in 0..length {
        for j in i+1..length {
            let (row_i, row_j) = matrix.split_at_mut(j);
            swap(&mut row_i[i][j], &mut row_j[0][i]);
        }
    }
    for row in matrix {
        row.reverse();
    }
}
*/