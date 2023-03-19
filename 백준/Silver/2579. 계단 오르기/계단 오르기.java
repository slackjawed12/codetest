import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 계단 오르기
 */
class Solution {
    public int solve(int N, int[] scores) {
        int[] dp = new int[301];
        if(N==1) return scores[1];
        
        dp[1] = scores[1];
        dp[2] = scores[1] + scores[2];
        for (int i = 3; i <= N; i++) {
            dp[i] =Math.max(dp[i - 3] + scores[i - 1], dp[i - 2])+scores[i];
        }
        return dp[N];
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    int[] scores;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, scores);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        scores = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            scores[i] = Integer.parseInt(rd.readLine());
        }
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}