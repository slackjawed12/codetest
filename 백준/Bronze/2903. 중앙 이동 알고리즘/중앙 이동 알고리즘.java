import java.io.*;

class Solution {
    public long solve(int N) {
        long p = (long)Math.pow(2, N);
        return (p + 1) * (p + 1);
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    long answer;

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