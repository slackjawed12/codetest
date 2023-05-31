import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Teacher {
    int[][] directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    public int searchMapBfs(Corridor corridor, int val) {
        boolean[][] visited = new boolean[corridor.ySize][corridor.xSize];
        int answer = 0;

        Queue<List<Integer>> q = new LinkedList<>();

        for (int i = 0; i < corridor.ySize; i++) {
            for (int j = 0; j < corridor.xSize; j++) {
                if (corridor.map[i][j] == val && !visited[i][j]) {
                    visited[i][j] = true;
                    q.add(List.of(i, j));
                    int cnt = 0;

                    while (!q.isEmpty()) {
                        List<Integer> next = q.poll();
                        for (int[] d : directions) {
                            int nx = next.get(1) + d[1];
                            int ny = next.get(0) + d[0];
                            if (nx >= 0 && nx < corridor.xSize && ny >= 0 && ny < corridor.ySize
                                    && corridor.map[ny][nx] == val
                                    && !visited[ny][nx]) {
                                visited[ny][nx] = true;
                                q.add(List.of(ny, nx));
                            }
                        }
                        cnt++;
                        answer = Math.max(cnt, answer);
                    }
                }
            }
        }

        return answer;
    }
}

class Corridor {
    int xSize;
    int ySize;
    int[][] map;

    public Corridor(int xSize, int ySize, int[][] map) {
        this.xSize = xSize;
        this.ySize = ySize;
        this.map = map;
    }
}

class Solution {
    public int solve(int N, int M, int[][] pos) {
        Teacher teacher = new Teacher();
        int[][] map = new int[N][M];
        int val = 1;
        for (int[] p : pos) {
            map[p[0] - 1][p[1] - 1] = val;
        }
        Corridor corridor = new Corridor(M, N, map);
        return teacher.searchMapBfs(corridor, val);
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N, M, K;
    int[][] pos;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, M, pos);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        K = Integer.parseInt(str[2]);
        pos = new int[K][2];
        for (int i = 0; i < K; i++) {
            pos[i] = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                    .toArray();
        }
    }


    public void output() throws Exception {
        wr.write(answer + "\n");
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
