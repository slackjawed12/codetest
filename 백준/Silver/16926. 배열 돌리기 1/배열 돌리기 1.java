import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

class Solution {
    public void rotateNumber(int[][] matrix, int[][] answer, int h, int w, int R, int depth) {
        int mod = 2 * (h + w) - 4;  // 사각형 둘레 한 바퀴

        // 0 ~ mod 까지 x, y 좌표 저장 배열
        int[][] posInfo = new int[mod][2];    // 0 : y, 1 : x, 위치 정보 설정

        // 사각형 꼭짓점 정수 정보
        int leftBottom = h - 1;
        int rightBottom = h + w - 2;
        int rightTop = 2 * h + w - 3;

        // depth에 대해 사각형 한 바퀴 돌면서 위치정보 저장 - depth는 offset으로 더해주면 됨
        for (int i = 0; i < mod; i++) {
            if (i < leftBottom) {    // 왼쪽 세로
                posInfo[i][0] = i + depth;
                posInfo[i][1] = depth;
            } else if (i < rightBottom) {   // 아래 가로
                posInfo[i][0] = h - 1 + depth;
                posInfo[i][1] = i - (h - 1) + depth;
            } else if (i < rightTop) {   // 오른쪽 세로
                posInfo[i][0] = 2 * h + w - 3 - i + depth;
                posInfo[i][1] = w - 1 + depth;
            } else {    // 윗 가로
                posInfo[i][0] = depth;
                posInfo[i][1] = 2 * (h + w) - 4 - i + depth;
            }
        }

        int r = R % mod;
        for (int i = 0; i < mod; i++) {
            int curX = posInfo[i][1];
            int curY = posInfo[i][0];
            int newX = posInfo[(i + r) % mod][1];
            int newY = posInfo[(i + r) % mod][0];
            answer[newY][newX] = matrix[curY][curX];
        }
    }

    public int[][] solve(int[][] matrix, int N, int M, int R) {
        int[][] answer = new int[N][M];
        int maxDepth = Math.min(N, M) / 2;
        int curDepth = 0;
        while (curDepth < maxDepth) {
            rotateNumber(matrix, answer, N, M, R, curDepth);
            curDepth++;
            N -= 2;
            M -= 2;
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    int M;
    int R;
    int[][] matrix;
    int[][] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(matrix, N, M, R);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        R = Integer.parseInt(str[2]);

        matrix = new int[N][M];
        for (int i = 0; i < N; i++) {
            String[] x = rd.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                matrix[i][j] = Integer.parseInt(x[j]);
            }
        }
    }

    public void output() throws Exception {
        for (int i = 0; i < answer.length; i++) {
            for (int j = 0; j < answer[i].length; j++) {
                System.out.print(answer[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
