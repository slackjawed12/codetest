import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Solution {
    public char[][] solve(String path) {
        int[][] dir = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
        int idx = 0;

        char[][] board = new char[101][101];
        int[] cur = new int[2];
        cur[0] = 50;    // x
        cur[1] = 50;    // y
        board[cur[1]][cur[0]] = '.';
        int xmax = cur[0], ymax = cur[1], xmin = cur[0], ymin = cur[1];

        for (int i = 0; i < path.length(); i++) {
            if (path.charAt(i) == 'R') {
                idx = (idx + 1) % 4;
            } else if (path.charAt(i) == 'L') {
                idx = idx == 0 ? 3 : (idx - 1) % 4;
            } else {
                cur[0] += dir[idx][0];
                cur[1] += dir[idx][1];
                xmax = Math.max(xmax, cur[0]);
                ymax = Math.max(ymax, cur[1]);
                xmin = Math.min(xmin, cur[0]);
                ymin = Math.min(ymin, cur[1]);
                board[cur[1]][cur[0]] = '.';
            }
        }

        char[][] answer = new char[ymax - ymin + 1][xmax - xmin + 1];
        for (int i = ymin; i <= ymax; i++) {
            for (int j = xmin; j <= xmax; j++) {
                if (board[i][j] != '.') {
                    answer[i - ymin][j - xmin] = '#';
                } else {
                    answer[i - ymin][j - xmin] = '.';
                }
            }
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    String path;
    char[][] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(path);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        path = rd.readLine();
    }


    public void output() throws Exception {
        for (int i = 0; i < answer.length; i++) {
            for (int j = 0; j < answer[i].length; j++) {
                wr.write(answer[i][j]);
            }
            wr.write("\n");
        }
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
