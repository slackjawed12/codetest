import java.io.*;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public String cantor(int len) {
        if (len == 1) {
            return "-";
        }
        return cantor(len/3).concat(" ".repeat(len/3)).concat(cantor(len/3));
    }

    public List<String> solve(List<Integer> N) {
        List<String> ans = new ArrayList<>();
        for (Integer i : N) {
            double d = Math.pow(3, i);
            ans.add(cantor((int)d));
        }
        return ans;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    List<Integer> N=new ArrayList<>();
    List<String> answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N);
        output();
    }

    public void input() throws Exception {
        String str;
        while ((str = rd.readLine()) != null) {
            N.add(Integer.parseInt(str));
        }
    }

    public void output() throws Exception {
        for (String s : answer) {
            wr.write(s + "\n");
        }
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}