import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        ArrayList<String> id_arraylist = new ArrayList<>(Arrays.asList(id_list));
        Set<String> report_set = new HashSet<>(Arrays.asList(report));
        
        ArrayList<String> reported_id_list = new ArrayList<>();
        for (String one_report : report_set) {
            reported_id_list.add(reported_id_list.size(), one_report.split(" ")[1]);
        }
        
        Map<String, Integer> reported_count_list = new HashMap<>();
        for (String id : reported_id_list) {
            reported_count_list.put(id, reported_count_list.getOrDefault(id, 0) + 1);
        }
        
        int[] answer = new int[id_list.length];
        int reported_count = 0;
        String reporting_user = "";
        for (String one_report : report_set) {
            reported_count = reported_count_list.getOrDefault(one_report.split(" ")[1], 0);
            reporting_user = one_report.split(" ")[0];
            if (reported_count >= k) {
                answer[id_arraylist.indexOf(reporting_user)] += 1;
            }
        }
        
        return answer;
    }
}