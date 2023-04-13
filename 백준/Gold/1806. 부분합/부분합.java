import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

class Solution {
    public int solve(int N, int S, int[] seq) {
        int min = 9999999;
        int cur = seq[0];
        int low = 0;
        int high = 0;
        while (high != N) {
            if (cur < S) {
                cur += seq[Math.min(++high, N-1)];
            } else {
                min = Math.min(high - low + 1, min);
                cur -= seq[low++];
            }
        }

        return min == 9999999 ? 0 : min;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    int S;
    int[] seq;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, S, seq);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        S = Integer.parseInt(str[1]);
        seq = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}