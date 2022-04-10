import java.util.*;

class Solution {
    public boolean isPrime(int n) {
        int[] primeLessThanRoot10000 = {2, 3, 5, 7, 11 ,13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 91, 97};
        
        for (int p : primeLessThanRoot10000) {
            if((n != p) && (n % p) == 0) {
                return false;
            }
        }
        
        return true;
    }
    
    public int solution(int[] nums) {
        // 중복제거하면 오답임...
        // Set<Integer> sums = new HashSet<>();
        ArrayList<Integer> sums = new ArrayList<>();
        int answer = 0;
        
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    sums.add(nums[i]+nums[j]+nums[k]);
                }
            }
        }
        System.out.println(sums);
        for (int n : sums) { 
            if (isPrime(n)) {
                answer += 1;
            }
        }

        return answer;
    }
}