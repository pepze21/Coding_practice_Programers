// 정확성 테스트는 통과했지만, 효율성 테스트에서 실패

function solution(s) {
    var i = 0;
      
    if (s.length % 2 === 1) {
      return 0;
    }
      
    while (i < s.length - 1) {
      if (s === '') {
        break;
      }
      i++;
      if (i === 0){
        i++;
      }
      if (s[i - 1] === s[i]) {
        s = s.slice(0, i - 1) + s.slice(i + 1)
        i -= 2;
      }
    }
  
    if (s === '') {
      return 1;
    } else {
      return 0;
    }
  }