import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 스티커
 */
class Solution {
    public int solve(int n, int[][] info) {
        int[][] dp = new int[2][n + 1];
        dp[0][1] = info[0][1];
        dp[1][1] = info[1][1];

        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < 2; j++) {
                dp[j][i] = Math.max(dp[j ^ 1][i - 1], dp[j ^ 1][i - 2]) + info[j][i];
            }
        }

        return Math.max(dp[0][n], dp[1][n]);
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    int T;
    int[] answer;

    public void submit() throws Exception {
        input();
        for (int i = 0; i < T; i++) {
            int n = Integer.parseInt(rd.readLine());
            int[][] info = new int[2][n + 1];
            for (int j = 0; j < 2; j++) {
                String str = rd.readLine();
                st = new StringTokenizer(str, " ");
                int k = 1;
                while (st.hasMoreTokens()) {
                    info[j][k++] = Integer.parseInt(st.nextToken());
                }
            }
            answer[i] = new Solution().solve(n, info);
        }
        output();
    }

    public void input() throws Exception {
        T = Integer.parseInt(rd.readLine());
        answer = new int[T];
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