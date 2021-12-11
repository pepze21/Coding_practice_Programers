function rotation(matrix, query) {
    let temp = 0;
    temp = matrix[query[0]][query[3]];
    let minimum = temp;
    
    for (var j = query[3]; j > query[1]; j--) {
      matrix[query[0]][j] = matrix[query[0]][j - 1];
      minimum = Math.min(minimum, matrix[query[0]][j - 1]);
    }
    for (var i = query[0]; i < query[2]; i++) {
      matrix[i][query[1]] = matrix[i + 1][query[1]];
      minimum = Math.min(minimum, matrix[i + 1][query[1]]);
    }
    for (var j = query[1]; j < query[3]; j++) {
      matrix[query[2]][j] = matrix[query[2]][j + 1];
      minimum = Math.min(minimum, matrix[query[2]][j + 1]);
    }
    for (var i = query[2]; i > query[0] + 1; i--) {
      matrix[i][query[3]] = matrix[i - 1][query[3]];
      minimum = Math.min(minimum, matrix[i - 1][query[3]]);
    }
    
    matrix[query[0] + 1][query[3]] = temp;
    return [matrix, minimum];
}

function solution(rows, columns, queries) {
  let row = new Array(columns).fill(0);
  let matrix = new Array(row);
  let num = 0;
  let result = -1;
  let answer = [];
    
  for (var i = 1; i <= rows; i++) {
    row = [0];
    for (var j = 1; j <= columns; j++) {
      num++;
      row.push(num);
    }
    matrix.push(row)
  }
    
  for (const query of queries) {
    [matrix, result] = rotation(matrix, query);
    answer.push(result);
  }

  return answer;
}