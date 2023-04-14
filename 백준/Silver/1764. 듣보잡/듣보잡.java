import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Set;
import java.util.TreeSet;
import java.util.stream.Collectors;

/**
 * 듣보잡
 */
class Solution {
    public Set<String> solve(String[] x, String[] y) {
        Set<String> answer = new TreeSet<>();

        Set<String> temp = Arrays.stream(x).collect(Collectors.toSet());
        Arrays.stream(y).forEach(e->{
            if(temp.contains(e)) {
                answer.add(e);
            }});
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    int M;
    String[] x;
    String[] y;
    Set<String> answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(x, y);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        x = new String[N];
        y = new String[M];
        for (int i = 0; i < N; i++) {
            x[i] = rd.readLine();
        }
        for (int i = 0; i < M; i++) {
            y[i] = rd.readLine();
        }
    }

    public void output() {
        System.out.println(answer.size());
        for (String s : answer) {
            System.out.println(s);
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}