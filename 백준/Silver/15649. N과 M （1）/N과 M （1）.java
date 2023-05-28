import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> solve(int N, int M,
                                     int[] info,
                                     List<Integer> path,
                                     List<List<Integer>> cur) {

        if (path.size() == M) { // depth = M
            List<Integer> made = new ArrayList<>(path);
            cur.add(made);
            return cur;
        }

        for (int i = 1; i <= N; i++) {
            if (info[i] != 1) {
                info[i] = 1;
                path.add(i);
                solve(N, M, info, path, cur);
                info[i] = 0;
                path.remove(path.size()-1);
            }
        }

        return cur;
    }

    public List<List<Integer>> solve(int N, int M) {
        return solve(N, M, new int[N + 1], new ArrayList<>(), new ArrayList<>());
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int M;
    List<List<Integer>> answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, M);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
    }


    public void output() throws Exception {
        for (List<Integer> i : answer) {
            for (Integer j : i) {
                wr.write(j + " ");
            }
            wr.write("\n");
        }
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
