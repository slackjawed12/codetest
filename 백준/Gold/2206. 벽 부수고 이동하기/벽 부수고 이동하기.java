import java.io.*;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

class Solution {
    int[][] direction = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    public int solve(int N, int M, int[][] map) {
        class State {
            final int x, y, length;
            final boolean hasBroken;

            public State(int x, int y, int length, boolean hasBroken) {
                this.x = x;
                this.y = y;
                this.length = length;
                this.hasBroken = hasBroken;
            }
        }

        int answer = Integer.MAX_VALUE;

        boolean[][] visit = new boolean[N][M];
        boolean[][] breakVisit = new boolean[N][M];
        Queue<State> q = new LinkedList<>();
        q.add(new State(0, 0, 1, false));
        visit[0][0] = true;

        while (!q.isEmpty()) {
            State cur = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = cur.x + direction[i][1];
                int ny = cur.y + direction[i][0];
                if (nx >= 0 && nx < M && ny >= 0 && ny < N) {
                    if(cur.hasBroken && breakVisit[ny][nx])
                        continue;
                    else if(!cur.hasBroken && visit[ny][nx])
                        continue;

                    if (map[ny][nx] == 1) {    // 벽 위치
                        if (!cur.hasBroken) {   // 안 깨고 온 경로
                            q.add(new State(nx, ny, cur.length + 1, true));
                            breakVisit[ny][nx]=true;
                        }
                    } else {
                        if(cur.hasBroken)
                            breakVisit[ny][nx]=true;
                        else
                            visit[ny][nx]=true;

                        q.add(new State(nx, ny, cur.length + 1, cur.hasBroken));
                    }
                }
            }

            if (cur.y == N - 1 && cur.x == M - 1) {
                answer = Math.min(answer, cur.length);
            }
        }

        return visit[N - 1][M - 1] || breakVisit[N - 1][M - 1] ? answer : -1;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N, M;
    int[][] map;
    Object answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, M, map);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        map = new int[N][M];
        for (int i = 0; i < N; i++) {
            String s = rd.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = s.charAt(j) - '0';
            }
        }
    }


    public void output() throws Exception {
        wr.write(String.valueOf(answer));
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}