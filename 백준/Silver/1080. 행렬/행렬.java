import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

class Solution {
    public int[][] flop(int[][] m, int x, int y) {
        for (int i = y - 1; i <= y + 1; i++) {
            for (int j = x - 1; j <= x + 1; j++) {
                m[i][j] = (m[i][j] == 0) ? 1 : 0;
            }
        }
        return m;
    }

    public int solve(int[][] A, int[][] B) {
        int answer = -1;
        int temp = 0;
        for (int i = 1; i < A.length - 1; i++) {
            for (int j = 1; j < A[0].length - 1; j++) {
                if (A[i - 1][j - 1] != B[i - 1][j - 1]) {
                    A = flop(A, j, i);
                    temp++;
                }
            }
        }
        if (Arrays.deepEquals(A, B)) answer = temp;

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    int M;
    int[][] A;
    int[][] B;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(A, B);
        output();
    }

    public int[][] matrixInput(int[][] m, int r, int c) throws Exception {
        for (int i = 0; i < r; i++) {
            String s = rd.readLine();
            for (int j = 0; j < c; j++) {
                m[i][j] = s.charAt(j) - '0';
            }
        }
        return m;
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        A = matrixInput(new int[N][M], N, M);
        B = matrixInput(new int[N][M], N, M);
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}