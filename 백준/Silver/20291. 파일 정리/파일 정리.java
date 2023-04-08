import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


/**
 * 파일 정리
 */
class Solution {
    public Map<String, Integer> solve(List<String> files) {
        Map<String, Integer> answer = new TreeMap<>();

        files.forEach(x -> {
            String ext = x.split("\\.")[1];
            answer.put(ext, answer.getOrDefault(ext, 0) + 1);
        });

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    Integer N;
    List<String> files;
    Map<String, Integer> answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(files);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        files = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            files.add(rd.readLine());
        }
    }

    public void output() {
        for (Map.Entry<String, Integer> e : answer.entrySet()) {
            System.out.println(e.getKey() + " " + e.getValue());
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}