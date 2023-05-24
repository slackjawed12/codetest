import java.util.Arrays.*;
class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int[][] dp = new int[triangle.length][];
        dp[0] = new int[1];
        dp[0][0] = triangle[0][0];
        
        for(int i=1; i<dp.length; i++){
            dp[i] = new int[i+1];
            for(int j=0; j<dp[i].length; j++) {
                int first = dp[i-1][Math.max(j-1,0)];
                int second = dp[i-1][Math.min(dp[i-1].length-1, j)];
                dp[i][j] = triangle[i][j] + Math.max(first, second);
            }
        }
        
        for(int i=0; i<dp[dp.length-1].length; i++){
            answer = Math.max(answer, dp[dp.length-1][i]);
        }
        
        return answer;
    }
}