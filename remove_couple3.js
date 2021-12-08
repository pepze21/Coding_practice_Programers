// 정확성 테스트도 통과 못하고, 효율성 테스트에서도 실패3333

function solution(s) {
  var visit = new Array(s.length);
  visit.fill(0);
  var i = 0;
  var left = 0;
  var right = 1;
  var count = 0;
    
  if (s.length % 2 === 1) {
      return 0;
  }

  while (right < s.length) {
    if ((left >= 0) && (s[left] === s[right])) {
      count++;
      visit[left] = 1;
      visit[right] = 1;
      
      while (visit[left] == 1) {
        left--;
      }
      right++;
    } else {
      left = right;
      right++;
    }
  }

  if (parseInt(s.length / 2) == count) {
    return 1;
  } else {
    return 0;
  }
}