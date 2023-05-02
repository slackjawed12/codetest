import java.io.*;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

class Solution {
    public int[] solve(int[] cards, int[] query) {
        int[] answer = new int[query.length];
        HashSet<Integer> cardSet = new HashSet<>();
        for (int x : cards) {
            cardSet.add(x);
        }

        for (int i = 0; i < query.length; i++) {
            answer[i] = cardSet.contains(query[i]) ? 1 : 0;
        }
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st; // 입력 많을 때 사용
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int M;
    int[] cards;
    int[] query;
    int[] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(cards, query);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        cards = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                .toArray();

        M = Integer.parseInt(rd.readLine());
        query = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                .toArray();
        answer = new int[M];
    }

    public void output() throws Exception {
        for (int j : answer) {
            wr.write(j + " ");
        }
        wr.write("\n");
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
