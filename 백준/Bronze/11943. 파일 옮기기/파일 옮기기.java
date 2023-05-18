import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Solution {
    public int solve(int A, int B, int C, int D) {
        return Math.min(A + D, B + C);
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int A, B, C, D;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(A, B, C, D);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        A = Integer.parseInt(str[0]);
        B = Integer.parseInt(str[1]);
        str = rd.readLine().split(" ");
        C = Integer.parseInt(str[0]);
        D = Integer.parseInt(str[1]);

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
