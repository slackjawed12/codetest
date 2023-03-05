import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    public int solve(int N, int[] arr) {
        int[] dp = new int[N];
        int temp = Math.max(arr[0], 0);
        dp[0] = arr[0];
        for (int i = 1; i < N; i++) {
            dp[i] = Math.max(temp + arr[i], dp[i - 1]);
            if (temp + arr[i] < 0) {
                temp = 0;
            } else {
                temp += arr[i];
            }
        }
        return dp[N-1];
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    int[] arr;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, arr);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        arr = new int[N];
        String[] str = rd.readLine().split(" ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(str[i]);
        }
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}