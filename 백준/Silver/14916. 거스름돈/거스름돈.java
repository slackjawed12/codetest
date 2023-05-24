import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Solution {
    public int solve(int n) {
        int answer = 0;
        answer += n / 5;
        n %= 5;
        while (n % 2 != 0 && answer > 0) {
            n += 5;
            answer--;
        }
        answer += n % 2 == 0 ? n / 2 : 0;
        return answer == 0 ? -1 : answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int n;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(n);
        output();
    }

    public void input() throws Exception {
        n = Integer.parseInt(rd.readLine());
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