import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

class Solution {
    public int solve(int N) {
        char[] x = String.valueOf(N).toCharArray();
        Arrays.sort(x);
        StringBuilder sb = new StringBuilder(String.valueOf(x));
        String temp = sb.reverse().toString();
        return Integer.parseInt(temp);
    }
}

public class Main {
    int N;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N);
        output();
    }

    public void input() throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String str = rd.readLine();
        N = Integer.parseInt(str);
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}