import java.io.*;
import java.util.StringTokenizer;

class Solution {
    public int solve(int S, int T, int D) {
        return (D / (2 * S)) * T;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st; // 입력 많을 때 사용
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int S;
    int T;
    int D;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(S, T, D);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        S=Integer.parseInt(str[0]);
        T=Integer.parseInt(str[1]);
        D=Integer.parseInt(str[2]);

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