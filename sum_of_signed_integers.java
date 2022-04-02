class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        int sign = 1;
        for (int i = 0; i < signs.length; i++) {
            if (signs[i] == true) {
                sign = 1;
            }
            else {
                sign = -1;
            }
            answer += (absolutes[i] * sign);
        }
        return answer;
    }
}