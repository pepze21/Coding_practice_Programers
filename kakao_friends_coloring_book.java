import java.util.*;

class Solution {
    
    private int m = 0;
    private int n = 0;
    private int[][] picture;
    private int numberOfArea = 0;
    private int sizeOfOneArea = 0;
    private int maxSizeOfOneArea = 0;
    
    // visit when color is not 0
    public void dfs(int i, int j, int color) {
        this.picture[i][j] = 0; // visit
        this.sizeOfOneArea += 1;
        if (i - 1 >= 0 && this.picture[i - 1][j] == color) {
            dfs(i - 1, j, color);
        }
        if (i + 1 < m && this.picture[i + 1][j] == color) {
            dfs(i + 1, j, color);
        }
        if (j - 1 >= 0 && this.picture[i][j - 1] == color) {
            dfs(i, j - 1, color);
        }
        if (j + 1 < n && this.picture[i][j + 1] == color) {
            dfs(i, j + 1, color);
        }
    }
    
    // There is an error in the problem itself
    // Deepcopy to fix the error
    public int[][] twoDimDeepcopy(int[][] twoDimArray) {
        int[][] result = new int[twoDimArray.length][twoDimArray[0].length];
        for (int i = 0; i < twoDimArray.length; i++) {
            for (int j = 0; j < twoDimArray[0].length; j++) {
                result[i][j] = twoDimArray[i][j];
            }
        }
        return result;
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        this.m = m;
        this.n = n;
        this.picture = twoDimDeepcopy(picture);

        for (int i = 0; i < m ; i++) {
            for (int j = 0; j < n ; j++) {
                if (this.picture[i][j] != 0) {
                    dfs(i, j, this.picture[i][j]);
                    this.numberOfArea += 1;
                    if (this.sizeOfOneArea > this.maxSizeOfOneArea) {
                        this.maxSizeOfOneArea = this.sizeOfOneArea;
                    }
                    this.sizeOfOneArea = 0;
                    // System.out.println("after " + this.numberOfArea + " times of dfs, this.picture is");
                    // for (int[] row : this.picture) {
                    //     System.out.println(Arrays.toString(row));
                    // }
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = this.numberOfArea;
        answer[1] = this.maxSizeOfOneArea;
        return answer;
    }
}