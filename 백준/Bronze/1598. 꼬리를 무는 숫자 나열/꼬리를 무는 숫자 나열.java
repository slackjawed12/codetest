import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    public int solve(int A, int B) {
        int x1 = (A - 1) / 4;
        int x2 = (B - 1) / 4;

        int y1 = (A + 3) % 4;
        int y2 = (B + 3) % 4;
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int A;
    int B;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(A, B);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        A = Integer.parseInt(str[0]);
        B = Integer.parseInt(str[1]);
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}