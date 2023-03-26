import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

class Solution {
    public int solve(int[][] record) {
        boolean[] hasSeen = new boolean[11];
        int[] position = new int[11];
        int answer = 0;
        for (int[] x : record) {
            int num = x[0];
            int pos = x[1];
            if (!hasSeen[num]) {
                hasSeen[num] = true;
            } else if (position[num] != pos) {
                answer++;
            }
            position[num] = pos;
        }
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    int[][] record;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(record);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        record = new int[N][2];
        for (int i = 0; i < N; i++) {
            record[i] = Arrays.stream(rd.readLine().split(" "))
                    .mapToInt(Integer::parseInt).toArray();
        }
    }

    public void output() throws Exception {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
