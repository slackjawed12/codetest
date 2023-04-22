import java.io.*;
import java.util.*;

class Solution {
    public List<Integer> solve(String[] operations) {
        List<Integer> ans = new ArrayList<>();
        Deque<Integer> q = new ArrayDeque<>();
        for (String op : operations) {
            String[] info = op.split(" ");
            if (info[0].equals("push")) {
                q.add(Integer.parseInt(info[1]));
            } else if (info[0].equals("size")) {
                ans.add(q.size());
            } else if (info[0].equals("empty")) {
                ans.add(q.isEmpty() ? 1 : 0);
            } else {
                if (q.isEmpty()) {
                    ans.add(-1);
                } else if (info[0].equals("pop")) {
                    ans.add(q.pollFirst());
                } else if (info[0].equals("front")) {
                    ans.add(q.peekFirst());
                } else {
                    ans.add(q.peekLast());
                }
            }
        }
        return ans;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    String[] operations;
    List<Integer> answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(operations);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        operations = new String[N];
        for (int i = 0; i < N; i++) {
            operations[i] = rd.readLine();
        }
    }

    public void output() throws Exception {
        for (Integer i : answer) {
            wr.write(String.valueOf(i) + "\n");
        }
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
