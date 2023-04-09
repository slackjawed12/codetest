import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    public int[] solve(int N, int M, int[][] info) {
        int[] answer = new int[N+1];
        for (int i = 0; i < M; i++) {
            for (int j = info[i][0]; j <= info[i][1]; j++) {
                answer[j]=info[i][2];
            }
        }
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    int M;
    int[][] info;
    int[] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, M, info);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        info = new int[M][3];
        answer=new int[N+1];
        for (int i = 0; i < M; i++) {
            str = rd.readLine().split(" ");
            info[i][0] = Integer.parseInt(str[0]);
            info[i][1] = Integer.parseInt(str[1]);
            info[i][2] = Integer.parseInt(str[2]);
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