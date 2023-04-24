import java.io.*;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public void solve(int N, int start, int from, int end, List<List<Integer>> move) {
        if (N == 0) {
            return;
        }
        solve(N - 1, start, end, from, move);
        move.add(List.of(start, end));
        solve(N - 1, from, start, end, move);
    }

    public List<List<Integer>> solve(int N) {
        List<List<Integer>> answer = new ArrayList<>();
        solve(N, 1, 2, 3, answer);
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    List<List<Integer>> answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
    }

    public void output() throws Exception {
        wr.write(answer.size() + "\n");
        for (List<Integer> move : answer) {
            wr.write(move.get(0) + " " + move.get(1) + "\n");
        }
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}