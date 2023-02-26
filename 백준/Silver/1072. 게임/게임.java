import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    public long solve(int X, int Y) {
        int low = 0;
        int high = X;
        int c;
        int Z = (int) ((long) Y * 100 / X);
        while (low <= high) {
            c = (low + high) / 2;
            if (((long) (Y + c) * 100) / (X + c) == Z) {
                low = c + 1;
            } else {
                high = c - 1;
            }
        }
        c = low;
        if (c > X) return -1;
        else return c;
    }
}

public class Main {
    int X;
    int Y;
    long answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(X, Y);
        output();
    }

    public void input() throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] str = rd.readLine().split(" ");
        X = Integer.parseInt(str[0]);
        Y = Integer.parseInt(str[1]);
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}