import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * 색종이
 */
class Solution {
    public int solve(int[][] positions) {
        int answer = 0;
        int[][] paper = new int[101][101];

        for (int[] position : positions) {
            int y = position[0];
            int x = position[1];
            for (int i = y; i < 10 + y; i++) {
                for (int j = x; j < 10 + x; j++) {
                    paper[i][j] = 1;
                }
            }
        }

        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                answer += paper[i][j] == 1 ? 1 : 0;
            }
        }
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;  // 색종이 수
    int[][] positions;  // 색종이 붙인 위치
    int answer; // 넓이

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(positions);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        positions = new int[N][2];
        for (int i = 0; i < N; i++) {
            positions[i] = Arrays.stream(rd.readLine().split(" "))
                    .mapToInt(Integer::parseInt).toArray();
        }
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
