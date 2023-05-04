import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;

class Solution {
    public List<String> solve(int M, String[] words) {
        List<String> answer = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();

        for (String word : words) {
            if (word.length() >= M) {
                if (!map.containsKey(word)) {
                    answer.add(word);
                }
                map.put(word, map.getOrDefault(word, 0) + 1);
            }
        }

        answer.sort((o1, o2) -> !map.get(o1).equals(map.get(o2)) ? map.get(o2) - map.get(o1)
                : o1.length() != o2.length() ? o2.length() - o1.length()
                : o1.compareTo(o2));

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int M;
    String[] words;
    List<String> answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(M, words);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        words = new String[N];
        for (int i = 0; i < N; i++) {
            words[i] = rd.readLine();
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
