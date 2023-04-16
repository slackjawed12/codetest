import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 팰린드롬인지 확인하기
 */
class Solution {
    public int solve(String x) {
        int len = x.length();
        for (int i = 0; i < len / 2; i++) {
            if (x.charAt(i) != x.charAt(len - i - 1)) {
                return 0;
            }
        }
        return 1;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    String word;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(word);
        output();
    }

    public void input() throws Exception {
        word = rd.readLine();
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}