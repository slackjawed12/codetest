import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(rd.readLine());
        String str = "";
        HashMap<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < N; i++) {
            List<Integer> adj = new ArrayList<>();
            graph.put(i, adj);
        }

        // 무향 그래프 초기화
        for (int i = 0; i < N; i++) {
            str = rd.readLine();
            for (int j = i + 1; j < str.length(); j++) {
                if (str.charAt(j) == 'Y') {
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }

        Set<Map.Entry<Integer, List<Integer>>> entrySet = graph.entrySet();
        int max = 0;
        for (Map.Entry<Integer, List<Integer>> entry : entrySet) {
            List<Integer> adj = entry.getValue();
            // 친구 정보
            boolean isFriend[] = new boolean[N];
            isFriend[entry.getKey()] = true;
            int temp = 0;
            for (int friend : adj) {
                if (!isFriend[friend]) {
                    temp++;
                    isFriend[friend] = true;
                }
                List<Integer> second = graph.get(friend);
                for (int next : second) {
                    if (!isFriend[next]) {
                        temp++;
                        isFriend[next] = true;
                    }
                }
            }
            if (max < temp) max = temp;
        }

        System.out.println(max);
    }
}