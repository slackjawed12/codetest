import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.stream.IntStream;

class Solution {
    public int[] solve(int N, int[][] operation) {
        int[] answer = IntStream.range(0, N+1).toArray();

        for (int[] op : operation) {
            int temp = answer[op[0]];
            answer[op[0]]=answer[op[1]];
            answer[op[1]]=temp;
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
        answer = new int[N+1];
        operation = new int[M][2];
        for (int i = 0; i < M; i++) {
            str=rd.readLine().split(" ");
            operation[i][0] = Integer.parseInt(str[0]);
            operation[i][1] = Integer.parseInt(str[1]);
        }
    }

    public void output() {
        for (int i = 1; i <= N; i++) {
            System.out.print(answer[i]+" ");
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}