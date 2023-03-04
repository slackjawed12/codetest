import java.io.*;
import java.util.*;

class Solution {
    public void makeTree(int start, int end, int level, int[] order, List<List<Integer>> ans) {
        if (start <= end) {
            int mid = (start + end) / 2;
            ans.get(level).add(order[mid]);
            makeTree(start, mid - 1, level + 1, order, ans);
            makeTree(mid + 1, end, level + 1, order, ans);
        }
    }

    public List<List<Integer>> solve(int K, int[] order) {
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < K; i++) {
            ans.add(new ArrayList<>());
        }
        makeTree(0, order.length - 1, 0, order, ans);

        return ans;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int K;
    int[] order;
    List<List<Integer>> answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(K, order);
        output();
    }

    public void input() throws Exception {
        K = Integer.parseInt(rd.readLine());
        String[] str = rd.readLine().split(" ");
        int num = 1 << K;
        order = new int[num - 1];
        for (int i = 0; i < str.length; i++) {
            order[i] = Integer.parseInt(str[i]);
        }
    }

    public void output() {
        for (int i = 0; i < answer.size(); i++) {
            for (int j = 0; j < answer.get(i).size(); j++) {
                System.out.print(answer.get(i).get(j) + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}