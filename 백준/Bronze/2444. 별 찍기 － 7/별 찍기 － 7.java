import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    public void solve(int N) {
        for (int i = 1; i <= 2 * N - 1; i++) {
            int cnt = i <= N ? 2 * i - 1 : 2 * (2 * N - i) - 1;
            System.out.print(" ".repeat((2 * N - 1 - cnt) / 2));
            System.out.print("*".repeat(cnt));
            if (i != 2 * N - 1) {
                System.out.println();
            }
        }
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;

    public void submit() throws Exception {
        input();
        new Solution().solve(N);
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}