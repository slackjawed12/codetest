import java.io.*;
import java.util.*;

class Solution {
    public int solve(int N, int[][] info) {
        class Node{    // 그래프의 정점 객체
            final int val;
            final int weight;

            public Node(int val, int weight) {
                this.val = val;
                this.weight = weight;
            }
        }

        boolean[] visit = new boolean[N+1]; // 방문정보 저장
        Map<Integer, List<Node>> graph = new HashMap<>();

        // 그래프 초기화
        for (int i = 1; i <= N; i++) {
            graph.put(i, new ArrayList<>());
        }

        // 인접리스트 초기화 - 방향성 없는 그래프
        for (int[] pair : info) {
            List<Node> adj1 = graph.get(pair[0]);
            List<Node> adj2 = graph.get(pair[1]);

            adj1.add(new Node(pair[1], 1));
            adj2.add(new Node(pair[0], 1));
        }

        // 우선순위 큐 초기화 - 첫 정점 대입
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.weight));
        int first = info[0][0];
        pq.add(new Node(first, 0));
        visit[first] = true;

        // 프림 알고리즘
        int answer = 0;
        while (!pq.isEmpty()){
            Node cur = pq.poll();
            answer += cur.weight;

            List<Node> nodes = graph.get(cur.val);

            for (Node node : nodes) {
                if(!visit[node.val]){
                    pq.add(node);
                    visit[node.val] = true;
                }
            }
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int T;
    int N;
    int M;
    int[][] info;
    int[] answer;

    public void submit() throws Exception {
        T = Integer.parseInt(rd.readLine());
        answer = new int[T];
        for (int i = 0; i < T; i++) {
            input();
            answer[i] = new Solution().solve(N, info);
        }
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        info = new int[M][2];
        for (int i = 0; i < M; i++) {
            info[i] = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                    .toArray();
        }
    }

    public void output() throws Exception {
        for (int i = 0; i < T; i++) {
            wr.write(answer[i] + "\n");
        }

        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
