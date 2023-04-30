import java.io.*;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solve(String[] S, String[] query) {
        int answer =0;
        Set<String> set = new HashSet<>();

        for (String s : S) {
            set.add(s);
        }

        for (String q : query) {
            if(set.contains(q)) {
                answer++;
            }
        }
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int M;
    String[] S;
    String[] query;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(S, query);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        S = new String[N];
        query = new String[M];
        for (int i = 0; i < N; i++) {
            S[i] = rd.readLine();
        }

        for (int i = 0; i < M; i++) {
            query[i] = rd.readLine();
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

