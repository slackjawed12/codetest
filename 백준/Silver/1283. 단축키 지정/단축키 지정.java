import java.io.*;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;


class Solution {
    public String[] solve(String[] options) {
        Set<Character> set = new HashSet<>();
        for (int i = 0; i < options.length; i++) {
            int pos = 0;    // 괄호 삽입 위치
            String[] words = options[i].split(" ");
            boolean flag = false;
            for (String word : words) { // 1 : 단어별로 단축키 지정 여부 체크
                char head = word.charAt(0) >= 'a' ?
                        (char) (word.charAt(0) - 32) : word.charAt(0);

                if (!set.contains(head)) { // 토큰의 첫글자가 set 들어있는지 확인
                    set.add(head);
                    flag = true;
                    break;
                }
                pos += word.length() + 1;
            }

            if (!flag) {  // 1에서 단축키 지정이 안 됨
                pos = 0;    // 삽입 위치 초기화
                for (int j = 0; j < options[i].length(); j++, pos++) { // 2단계 적용
                    // 'A' : 65, 'a' : 97
                    char key = options[i].charAt(j) >= 'a' ?
                            (char) (options[i].charAt(j) - 32) : options[i].charAt(j);

                    if (!set.contains(key) && 'A' <= key && key <= 'Z') {
                        set.add(key);
                        flag = true;
                        break;
                    }
                }
            }

            if (flag) {
                StringBuilder sb = new StringBuilder(options[i]);
                sb.insert(pos, "[");
                sb.insert(pos + 2, "]");
                options[i] = sb.toString();
            }
        }
        return options;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    String[] options;
    String[] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(options);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        options = new String[N];
        answer = new String[N];

        for (int i = 0; i < N; i++) {
            options[i] = rd.readLine();
        }
    }


    public void output() throws Exception {
        for (String x : answer) {
            wr.write(x + "\n");
        }
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
