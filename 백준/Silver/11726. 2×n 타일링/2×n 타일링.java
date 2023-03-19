import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    public int solve(int n) {
        int[] dp = new int[1001];

        dp[1] = 1;
        dp[2] = dp[1] + 1;
        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i - 1] % 10007 + dp[i - 2] % 10007) % 10007;
        }

        return dp[n];
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int n;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(n);
        output();
    }

    public void input() throws Exception {
        n = Integer.parseInt(rd.readLine());
    }


    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}