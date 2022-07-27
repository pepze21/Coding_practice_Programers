import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        Arrays.sort(jobs, Comparator.comparingInt(o1 -> o1[0]));
        int fin_time = 0;
        int sum_time = 0;
        
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] job1, int[] job2) {
                return job1[1] - job2[1]; // 오름차순
            }
        });
        
        int i = 0;
        int[] next_job = jobs[0];
        
        while ((i < jobs.length) || !(pq.isEmpty())) {
            if (pq.isEmpty() && (jobs[i][0] > fin_time)) {
                fin_time = jobs[i][0];
            }
            while ((i < jobs.length)  && (jobs[i][0] <= fin_time)) {
                pq.add(jobs[i]);
                i++;
            }
            if (!pq.isEmpty()) {
                next_job = pq.poll();
                fin_time += next_job[1];
                sum_time += (fin_time - next_job[0]);
            }
        }
        // System.out.println(next_job);
        // System.out.println(fin_time);
        // System.out.println(sum_time);
        // System.out.println(sum_time/jobs.length);
        
        int answer = (int)(sum_time / jobs.length);
        
        return answer;
    }
}