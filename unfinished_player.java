import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> participant_map = new HashMap<>();
        String answer = "";
        int count = 0;
        
        for (String name : participant) {
            count = participant_map.containsKey(name) ? participant_map.get(name) + 1 : 1;
            participant_map.put(name, count);
        }
        
        for (String name : completion) {
            count = participant_map.get(name) - 1;
            if (count > 0) {
                participant_map.put(name, count);
            } else {
                participant_map.remove(name);
            }
        }
        
        // // participant_map.entrySet()은 key=value 쌍이 필요할 때 사용
        // for (Map.Entry<String, Integer> entry : participant_map.entrySet()) {
        //     System.out.println(entry);
        // }
        
        for (String name : participant_map.keySet()) {
            answer = name;
        }
        
        return answer;
    }
}