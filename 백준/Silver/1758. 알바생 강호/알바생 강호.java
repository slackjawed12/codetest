import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

class Solution {
    public long solve(int[] tips) {
        long[] sorted = Arrays.stream(tips).boxed()
                .sorted((o1, o2) -> o2 - o1).mapToLong(Long::valueOf).toArray();

        for (int i = 0; i < sorted.length; i++) {
            sorted[i] = Math.max(sorted[i] - i, 0);
        }

        return Arrays.stream(sorted).sum();
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int[] tips;
    long answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(tips);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        tips = new int[N];
        for (int i = 0; i < N; i++) {
            tips[i] = Integer.parseInt(rd.readLine());
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
