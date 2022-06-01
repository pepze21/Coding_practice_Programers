function solution(s) {
  var arr = new Array(s[0]);
  for (var i = 1; i < s.length; i++) {
    if (s[i] !== arr[arr.length - 1]) {
      arr.push(s[i]);
    } else {
      arr.pop();
    }
  }
  if (arr.length === 0) {
    return 1;
  } else {
    return 0;
  }
}