import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Trie {
    String data = "";
    TreeMap<String, Trie> child = new TreeMap<>();

    public Trie add(String str) {
        return child.put(str, child.getOrDefault(str, new Trie()).add(str));
    }

    public void add(List<String> seq, int pos) {
        if (pos != seq.size()) {
            String token = seq.get(pos);
            child.put(token, child.getOrDefault(token, new Trie()));

            Trie next = child.get(token);
            next.data = token;

            next.add(seq, pos + 1);
        }
    }

    public void print(String dash) {
        System.out.println(dash + data);
        if (child != null) {
            dash = dash.concat("--");
            for (Map.Entry<String, Trie> entry : child.entrySet()) {
                entry.getValue().print(dash);
            }
        }
    }
}

class Solution {
    public Trie solve(List<List<String>> infos) {
        Trie answer = new Trie();

        for (List<String> info : infos) {
            answer.add(info, 0);
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    List<List<String>> infos;
    Trie answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(infos);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        infos = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            List<String> info = new ArrayList<>();
            String[] str = rd.readLine().split(" ");
            int K = Integer.parseInt(str[0]);
            for (int j = 1; j <= K; j++) {
                info.add(str[j]);
            }
            infos.add(info);
        }
    }

    public void output() {
        for (Map.Entry<String, Trie> entry : answer.child.entrySet()) {
            entry.getValue().print("");
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}