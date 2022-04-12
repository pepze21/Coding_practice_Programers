import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] scores = new int[4]; // scores[1]이 1번 수포자 점수
        int max_score = 0;
        
        int[][] table = {{},
                         {1, 2, 3, 4, 5},
                         {2, 1, 2, 3, 2, 4, 2, 5},
                         {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == table[1][i % table[1].length])
                scores[1] += 1;
            if (answers[i] == table[2][i % table[2].length])
                scores[2] += 1;
            if (answers[i] == table[3][i % table[3].length])
                scores[3] += 1;
        }
        // System.out.println("scores : "+Arrays.toString(scores));
        
        for (int score : scores) {
            if (score > max_score) {
                max_score = score;
            }
        }
        // System.out.println("max_score : " + max_score);
        int array_size = 0;
        for (int i = 1; i <= 3; i++) {
            if (scores[i] == max_score) {
                array_size += 1;
            }
        }
        // System.out.println("array_size : " + array_size);
        int[] winners = new int[array_size];
        int index = -1;
        for (int i = 1; i <= 3; i++) {
            if (scores[i] == max_score) {
                index += 1;
                winners[index] = i;
            }
        }
        // System.out.println("winners : "+Arrays.toString(winners));
        return winners;
    }
}