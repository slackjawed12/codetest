import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Solution {
    public int solve(int[] coins, int k) {
        HashSet<Integer> set = new HashSet<>();
        for (Integer c : coins) {
            set.add(c);
        }

        Queue<Integer> q = new LinkedList<>();
        int[] info = new int[k + 1];
        Arrays.fill(info, -1);
        for (Integer e : set) { // info update, queue push
            if (e <= k) info[e] = 1;
            q.offer(e);
        }

        while (!q.isEmpty()) {
            int curValue = q.peek();
            for (Integer i : set) {
                int t = curValue + i;
                if (t <= k) {
                    if (info[t] == -1) {
                        info[t] = info[curValue] + 1;
                        q.offer(t);
                    } else if (info[t] > info[curValue] + 1) {
                        info[t] = info[curValue] + 1;
                        q.offer(t);
                    }
                }
            }
            q.poll();
        }
        return info[k];
    }
}

public class Main {
    int[] coins;
    int k;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(coins, k);
        output();
    }

    public void input() throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] str = rd.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        k = Integer.parseInt(str[1]);
        coins = new int[n];
        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(rd.readLine());
        }
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}