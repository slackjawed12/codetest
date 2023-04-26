import java.io.*;
import java.util.*;

class Solution {
    public List<Integer> solve(int N, int[][] compare) {
        List<Integer> answer = new ArrayList<>();
        int[] inDegree = new int[N + 1];
        Map<Integer, List<Integer>> adj = new HashMap<>();

        // adj 초기화
        for (int i = 1; i <= N; i++) {
            adj.put(i, new ArrayList<>());
        }

        for (int[] info : compare) {
            List<Integer> list = adj.get(info[0]);
            list.add(info[1]);
            adj.put(info[0], list);
            inDegree[info[1]]++;
        }

        // bfs
        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 1; i < inDegree.length; i++) {
            if (inDegree[i] == 0) {
                q.add(i);
            }
        }

        while (!q.isEmpty()) {
            int x = q.poll();
            List<Integer> list = adj.get(x);
            for (Integer i : list) {
                inDegree[i]--;
                if (inDegree[i] == 0) {
                    q.add(i);
                }
            }
            answer.add(x);
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int M;
    int[][] compare;
    List<Integer> answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, compare);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);

        M = Integer.parseInt(str[1]);
        compare = new int[M][2];
        for (int i = 0; i < M; i++) {
            compare[i] = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                    .toArray();
        }
    }

    public void output() throws Exception {
        for (int i : answer) {
            wr.write(i + " ");
        }
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
