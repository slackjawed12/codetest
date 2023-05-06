import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

class Solution {
    public int solve(int K, int[] sequence) {
        int answer = 0;
        for (int i = 0; i < K; i++) {
            answer += sequence[i];
        }

        int partial = answer;
        for (int i = 1; i < sequence.length - K + 1; i++) {
            partial += sequence[i + K - 1] - sequence[i - 1];
            if (partial > answer) {
                answer = partial;
            }
        }
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int K;
    int[] sequence;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(K, sequence);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        K = Integer.parseInt(str[1]);
        sequence = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                .toArray();
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