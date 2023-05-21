import java.io.*;
import java.util.Arrays;

class Solution {
    // O(n^2) 풀이
    public int solve(int[] boxSize) {
        int[] dp = new int[boxSize.length + 1];
        int answer = 0;
        // dp : 해당 인덱스까지 가장 긴 증가 부분 수열
        for (int i = 1; i < dp.length; i++) {
            dp[i] = 1;
            for (int j = 1; j <= i; j++) {
                if (boxSize[i - 1] > boxSize[j - 1]) {  // 이전(j) 값이 현재(i) 값보다 작으면
                    // (j 위치의 LIS 길이 + 1)과 현재까지 갱신된 LIS 길이 중 최댓값 선택
                    dp[i] = Math.max(dp[j] + 1, dp[i]);
                }
            }
            answer = Math.max(dp[i], answer);
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int[] boxSize;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(boxSize);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        boxSize = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                .toArray();

    }


    public void output() throws Exception {
        wr.write(String.valueOf(answer));
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
