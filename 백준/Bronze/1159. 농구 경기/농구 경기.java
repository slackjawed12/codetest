import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(rd.readLine());
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < N; i++) {
            char c = rd.readLine().charAt(0);
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        List<Character> answer = new ArrayList<>();
        Set<Map.Entry<Character, Integer>> entries = map.entrySet();
        for (Map.Entry<Character, Integer> e : entries) {
            if (e.getValue() >= 5) answer.add(e.getKey());
        }
        if(answer.size()==0) {
            System.out.println("PREDAJA");
        }
        else {
            answer.sort((o1, o2) -> o1 - o2);
            answer.forEach(System.out::print);
        }
    }
}