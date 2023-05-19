import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

class Solution {
    public int solve(int N, int S, int P, int[] scores) {
        if (N == 0) {
            return 1;
        }

        int rank = 1;   // 랭킹
        int i = 0;      // 인덱스
        int before = S;
        int current;
        while (i < N && S <= scores[i]) {
            current = scores[i];
            if (current != before) {  // 현재값이 이전값과 다르면
                rank = i + 1;   // 랭킹을 인덱스+1로 갱신
            }
            before = current;
            i++;
        }

        if (i == N && N == P) {
            rank = -1;
        } else if (before != S) {
            rank = i + 1;
        }

        return rank;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int S;
    int P;
    int[] scores;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, S, P, scores);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        S = Integer.parseInt(str[1]);
        P = Integer.parseInt(str[2]);

        if (N > 0) {
            scores = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                    .toArray();
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
