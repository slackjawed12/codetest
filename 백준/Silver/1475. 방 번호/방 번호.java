import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Solution {
    public int solve(int N) {
        int[] info = new int[10];
        while (N != 0) {
            info[N % 10]++;
            N /= 10;
        }

        int max = (info[6] + info[9] + 1) / 2;
        for (int i = 0; i < info.length; i++) {
            if (i != 6 && i != 9) {
                max = Math.max(info[i], max);
            }
        }

        return max;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
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
