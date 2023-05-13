import java.io.*;
import java.time.LocalDate;
import java.util.StringTokenizer;

class Solution {
    public String solve(int A, int B) {
        LocalDate test = LocalDate.of(2015, A, B);
        LocalDate cmp = LocalDate.of(2015, 2, 18);
        if (test.isEqual(cmp)) {
            return "Special";
        } else if (test.isBefore(cmp)) {
            return "Before";
        } else {
            return "After";
        }
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int A;
    int B;
    String answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(A, B);
        output();
    }

    public void input() throws Exception {
        A = Integer.parseInt(rd.readLine());
        B = Integer.parseInt(rd.readLine());
    }


    public void output() throws Exception {
        wr.write(answer);
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}