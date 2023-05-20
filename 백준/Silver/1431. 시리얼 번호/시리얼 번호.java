import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String[] solve(String[] serials) {
        class Cmp implements Comparator<String> {
            public int compare(String o1, String o2) {
                if (o1.length() != o2.length()) {   // 길이가 다를 경우
                    return o1.length() - o2.length();
                } else {    // 길이가 같으면
                    int sum1 = o1.chars().filter(x -> x >= '0' && x <= '9').map(x -> x - '0').sum();
                    int sum2 = o2.chars().filter(x -> x >= '0' && x <= '9').map(x -> x - '0').sum();
                    if (sum1 != sum2) { // 자릿수의 합 비교
                        return sum1 - sum2;
                    } else {    // 자릿수 합이 같으면 사전순
                        return o1.compareTo(o2);
                    }
                }
            }
        }

        return Arrays.stream(serials).sorted(new Cmp()).toArray(String[]::new);
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    String[] serials;
    String[] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(serials);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        serials = new String[N];
        for (int i = 0; i < N; i++) {
            serials[i] = rd.readLine();
        }
    }


    public void output() throws Exception {
        for (String s : answer) {
            wr.write(s + "\n");
        }
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
