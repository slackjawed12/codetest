import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.stream.IntStream;

class Solution {
    public int[] solve(int N, int[][] operation) {
        int[] answer = IntStream.range(0, N + 1).toArray();
        for (int[] op : operation) {
            int len = op[1] - op[0] + 1;
            int[] temp = new int[len];
            for (int i = 0; i < len; i++) {
                int idx = i + op[0];
                int target = (i + op[1] - op[2] + 1) % len;
                temp[target] = answer[idx];
            }
            
            for (int k = op[0]; k <= op[1]; k++) {
                answer[k] = temp[k - op[0]];
            }
        }
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    int M;
    int[][] operation;
    int[] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, operation);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        operation = new int[M][3];
        for (int i = 0; i < M; i++) {
            str = rd.readLine().split(" ");
            operation[i][0] = Integer.parseInt(str[0]);
            operation[i][1] = Integer.parseInt(str[1]);
            operation[i][2] = Integer.parseInt(str[2]);
        }
    }

    public void output() {
        for (int i = 1; i < answer.length; i++) {
            System.out.print(answer[i] + " ");
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}