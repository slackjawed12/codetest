import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    public int solve(int n, int[] wines) {
        int[] dp = new int[n + 1];
        dp[1] = wines[0];
        int conti = 1;
        for (int i = 2; i <= n; i++) {
            if (conti == 2) {
                int choice = 0;
                int before = 0;
                int max = 0;
                for (int j = 1; j <= Math.min(3, i); j++) {
                    before += dp[i - j];
                    if (max < choice + before) {
                        max = choice + before;
                        conti = j - 1;
                    }
                    choice += wines[i - j];
                    before -= dp[i - j];
                }
                dp[i] = max;
            } else {
                dp[i] = dp[i - 1] + wines[i - 1];
                conti++;
            }
        }
        return dp[n];
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int n;
    int[] wines;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(n, wines);
        output();
    }

    public void input() throws Exception {
        n = Integer.parseInt(rd.readLine());
        wines = new int[n];
        String str;
        for (int i = 0; i < n; i++) {
            str = rd.readLine();
            wines[i] = Integer.parseInt(str);
        }
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}