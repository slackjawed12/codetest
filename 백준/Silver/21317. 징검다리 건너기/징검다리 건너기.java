import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * 징검다리 건너기
 */
class Solution {
    public int solve(int N, int K, int[][] jumps) {
        // 매우 큰 점프 : dp[0][i] - 안 씀, dp[1][i] - 씀
        int[][] dp = new int[2][21];

        // 이론 상 최댓값 이상으로 초기화
        Arrays.fill(dp[0], 99999999);
        Arrays.fill(dp[1], 99999999);

        // 안 썼을 때 앞부분 초기값 설정
        dp[0][1] = 0;
        dp[0][2] = jumps[0][0];
        if (N >= 3) {
            dp[0][3] = Math.min(dp[0][2] + jumps[1][0], dp[0][1] + jumps[0][1]);
        }

        for (int i = 4; i <= N; i++) {
            // dp[0][i] (안 썼을 때) : i-1+작은점프와 i-2+큰 점프 중 최솟값
            dp[0][i] = Math.min(dp[0][i - 1] + jumps[i - 2][0], dp[0][i - 2] + jumps[i - 3][1]);
            // dp[1][i] (썼을 때)
            int min = Math.min(dp[1][i - 1] + jumps[i - 2][0], dp[1][i - 2] + jumps[i - 3][1]);
            dp[1][i] = Math.min(min, dp[0][i - 3] + K);
        }
        return Math.min(dp[0][N], dp[1][N]);
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    int[][] jumps;
    int K;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, K, jumps);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        jumps = new int[21][2];
        for (int i = 0; i < N - 1; i++) {
            String[] str = rd.readLine().split(" ");
            jumps[i][0] = Integer.parseInt(str[0]);
            jumps[i][1] = Integer.parseInt(str[1]);
        }
        K = Integer.parseInt(rd.readLine());
    }


    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}