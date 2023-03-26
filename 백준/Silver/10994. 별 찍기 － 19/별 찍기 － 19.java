import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 별 찍기 - 19
 */
class Solution {
    // 2차원 배열에 길이가 l이고 문자가 c인 사각형 입력
    public void printSquare(char[][] mat, int l, int depth, char c) {
        for (int i = depth; i < l + depth; i++) mat[depth][i] = c;  // 윗 가로
        for (int i = depth; i < l + depth; i++) mat[i][depth] = c;  // 왼쪽 세로
        for (int i = depth; i < l + depth; i++) mat[depth + l - 1][i] = c;  // 오른쪽 세로
        for (int i = depth; i < l + depth; i++) mat[i][depth + l - 1] = c;  // 아래 가로
    }

    public void solve(int N) {
        int L = 4 * N - 3;
        char[][] output = new char[L][L];
        int depth = 0;
        while (depth <= 2 * (N - 1)) {
            printSquare(output, L, depth, depth % 2 == 0 ? '*' : ' ');
            depth++;
            L -= 2;
        }

        for (int i = 0; i < 4 * N - 3; i++) {
            for (int j = 0; j < 4 * N - 3; j++) {
                System.out.print(output[i][j]);
            }
            System.out.println();
        }
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;

    public void submit() throws Exception {
        input();
        new Solution().solve(N);
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}