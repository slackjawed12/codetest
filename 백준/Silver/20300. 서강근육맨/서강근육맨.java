import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution {
    public long solve(long[] t) {
        long[] sorted = Arrays.stream(t).sorted().toArray();
        long answer = sorted[0];

        for (int i = 0; i < t.length / 2; i++) {
            int j = t.length % 2 == 0 ? t.length - i - 1 : t.length - i - 2;
            answer = Math.max(sorted[i] + sorted[j], answer);
        }

        if (t.length % 2 != 0) {
            answer = Math.max(sorted[sorted.length - 1], answer);
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    long[] t;
    long answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(t);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        t = Arrays.stream(rd.readLine().split(" ")).mapToLong(Long::parseLong)
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
