import java.io.*;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.TreeSet;

/**
 * 행복 유치원
 * N개의 정렬된 데이터를 K개 묶음으로 나눴을 때
 * 각 K개 묶음의 (최대-최소)의 합이 최소가 되도록 구성하고 그 최솟값을 출력
 * 1 <= K <= N <= 300,000
 */
class Solution {
    // 아이디어 1 : 각 데이터의 차이를 구하고, 최대 차이 k개에 대해 묶음 처리
    public int solve(int K, int[] heights) {
        class Point {
            final int diff;
            final int index;

            Point(int diff, int index) {
                this.diff = diff;
                this.index = index;
            }
        }

        // 1. diff, index pair 자료구조에 저장 (PriorityQueue) O(n)
        // 2. index 큰 순서로 자료구조에 저장 (TreeSet) O(k)
        // 3. 인덱스 묶음에 대해 합 계산 O(k)
        PriorityQueue<Point> q = new PriorityQueue<>((o1, o2) -> o1.diff != o2.diff ? o1.diff - o2.diff :
                o1.index - o2.index);

        for (int i = 1; i < heights.length; i++) {
            int newDiff = heights[i] - heights[i - 1];
            if (q.size() < K - 1) {
                q.add(new Point(newDiff, i));
            } else if (q.size() > 0) {
                if (q.peek().diff < newDiff) {
                    q.poll();
                    q.add(new Point(newDiff, i));
                }
            }
        }

        TreeSet<Integer> indexSet = new TreeSet<>();
        for (Point point : q) {
            indexSet.add(point.index);
        }

        int begin = 0;
        int answer = 0;
        for (Integer i : indexSet) {
            answer += heights[i - 1] - heights[begin];
            begin = i;
        }
        
        answer += heights[heights.length - 1] - heights[begin];
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int K;
    int[] heights;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(K, heights);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        K = Integer.parseInt(str[1]);
        heights = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                .toArray();

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
