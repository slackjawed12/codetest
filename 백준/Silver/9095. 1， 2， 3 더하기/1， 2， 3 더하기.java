import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 1,2,3 더하기
 */
class Solution {
    public int solve(int N) {
        int[] dp = new int[N + 1];
        for (int i = 1; i <= Math.min(3, N); i++) {
            dp[i] = 1;
        }

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= Math.min(3, i); j++) {
                dp[i] += dp[i - j];
            }
        }

        return dp[N];
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int T;
    int[] N;
    int[] answer;

    public void submit() throws Exception {
        input();
        for (int i = 0; i < T; i++) {
            answer[i] = new Solution().solve(N[i]);
        }
        output();
    }

    public void input() throws Exception {
        T = Integer.parseInt(rd.readLine());
        N = new int[T];
        answer = new int[T];

        for (int i = 0; i < T; i++) {
            N[i] = Integer.parseInt(rd.readLine());
        }
    }


    public void output() {
        for (int ans : answer) {
            System.out.println(ans);
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}