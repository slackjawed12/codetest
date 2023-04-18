import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    public String solve(String[] words) {
        String answer = "";
        for (int i = 0; i < 15; i++) {
            for (int j = 0; j < words.length; j++) {
                if (i < words[j].length()) {
                    answer = answer + words[j].charAt(i);
                }
            }
        }
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    String[] words;
    String answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(words);
        output();
    }

    public void input() throws Exception {
        words=new String[5];
        for (int i = 0; i < 5; i++) {
            words[i] = rd.readLine();
        }
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}