import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    public int solve(int N, int[][] price) {
        int minPackage = price[0][0], minEach = price[0][1];
        for (int[] x : price) {
            if (minPackage > x[0]) minPackage = x[0];
            if (minEach > x[1]) minEach = x[1];
        }

        int answer = 0;
        while (N > 6) {
            int cheap = Math.min(6 * minEach, minPackage);
            answer += cheap;
            N -= 6;
        }
        answer += Math.min(N * minEach, minPackage);
        return answer;
    }
}

public class Main {
    int N;
    int M;
    int[][] price;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, price);
        output();
    }

    public void input() throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        price = new int[M][2];
        for (int i = 0; i < M; i++) {
            String[] p = rd.readLine().split(" ");
            price[i][0] = Integer.parseInt(p[0]);
            price[i][1] = Integer.parseInt(p[1]);
        }
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}