import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] gymSuit = new int[n + 2]; // 0, n + 1은 안쓰는 index (boundary)
        Arrays.fill(gymSuit, 1);
        for (int index : lost) {
            gymSuit[index] -= 1;
        }
        for (int index : reserve) {
            gymSuit[index] += 1;
        }
        
        for (int i = 1; i <= n; i++) {
            if (gymSuit[i] == 0) {
                if (gymSuit[i - 1] == 2) {
                    gymSuit[i - 1] -= 1;
                    gymSuit[i] += 1;
                } else if ((gymSuit[i + 1] == 2)) {
                    gymSuit[i + 1] -= 1;
                    gymSuit[i] += 1;
                }
            }
        }
        
        for (int i = 1; i <= n; i++) {
            if (gymSuit[i] >= 1) {
                answer += 1;
            }
        }

        return answer;
    }
}