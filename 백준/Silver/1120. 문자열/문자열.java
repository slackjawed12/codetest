import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    public int solve(String A, String B) {
        int answer = 0;
        int max = 0;
        for (int i = 0; i <= B.length() - A.length(); i++) {
            int temp = 0;
            for (int j = 0; j < A.length(); j++) {
                if (A.charAt(j) == B.charAt(j + i)) {
                    temp++;
                }
            }
            if (max < temp) max = temp;
        }
        answer = A.length() - max;
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    String A;
    String B;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(A, B);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        A = str[0];
        B = str[1];
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}