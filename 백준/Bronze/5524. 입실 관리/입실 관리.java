import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> solve(String[] strings) {
        List<String> answer = new ArrayList<>();

        for (String string : strings) {
            answer.add(string.toLowerCase());
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    String[] strings;
    List<String> answer=new ArrayList<>();

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(strings);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        strings = new String[N];
        for (int i = 0; i < N; i++) {
            strings[i]= rd.readLine();
        }
    }


    public void output() throws Exception {
        for (String s : answer) {
            wr.write(s+"\n");
        }
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}