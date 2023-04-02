import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

class Solution {
    public int[] solve(int[] switches, int[][] info) {
        for (int[] op : info) {
            if (op[0] == 1) {   // 남학생
                int idx = op[1] - 1;
                for (int i = idx; i < switches.length; i += op[1]) {
                    switches[i] ^= 1;
                }
            }

            if (op[0] == 2) {   // 여학생
                int idx = op[1] - 1;
                switches[idx] ^= 1;
                int left = idx - 1;
                int right = idx + 1;
                while (left >= 0 && right < switches.length && switches[left] == switches[right]) {
                    switches[left--] ^= 1;
                    switches[right++] ^= 1;
                }
            }
        }

        return switches;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    int[] switches;
    int S;
    int[][] info;
    int[] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(switches, info);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        switches = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        S = Integer.parseInt(rd.readLine());
        info = new int[S][2];
        for (int i = 0; i < S; i++) {
            info[i] = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
    }

    public void output() throws Exception {
        for (int i = 0; i < answer.length; i++) {
            System.out.print(answer[i] + " ");
            if (i % 20 == 19) {
                System.out.println();
            }
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}