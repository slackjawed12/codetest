import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Solution {
    public String solve(String board) {
        String answer = "";
        int cnt = 0;
        for (int i = 0; i < board.length(); i++) {
            if (board.charAt(i) == 'X') {
                cnt++;
            } else {
                if (cnt % 2 != 0) {
                    return "-1";
                }
                
                while (cnt != 0) {
                    if (cnt >= 4) {
                        answer = answer.concat("AAAA");
                        cnt -= 4;
                    } else {
                        answer = answer.concat("BB");
                        cnt -= 2;
                    }
                }
                answer = answer.concat(".");
            }
        }

        if (cnt % 2 != 0) {
            return "-1";
        }

        while (cnt != 0) {
            if (cnt >= 4) {
                answer = answer.concat("AAAA");
                cnt -= 4;
            } else {
                answer = answer.concat("BB");
                cnt -= 2;
            }
        }
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    String board;
    String answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(board);
        output();
    }

    public void input() throws Exception {
        board = rd.readLine();
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
