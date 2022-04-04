import java.util.*;

class Solution {
    public int solution(int[] nums) {
        
        Set<Integer> nums_set = new HashSet<>();
        for (int num : nums) {
            nums_set.add(num);
        }
        
        return Math.min(nums_set.size(), nums.length/2);
    }
}