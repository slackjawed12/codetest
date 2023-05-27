import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

class Solution {
    // 아이디어 1 : 정렬 후 작은 순서대로 합치기
    // 문제 : 합치는 중에 최소 묶음이 바뀔 수 있다.
    // 아이디어 2 : 합치면서 최솟값을 유지 - PriorityQueue (중복때문에 TreeSet 불가)
    public long solve(int[] sizes) {
        PriorityQueue<Long> queue = Arrays.stream(sizes).mapToLong(x->(long)x)
                .boxed().collect(Collectors.toCollection(PriorityQueue::new));

        long deck = queue.poll();
        long answer = 0;

        while (!queue.isEmpty()) {
            if (deck > queue.peek()) {
                queue.add(deck);
                deck = queue.poll();
                if (!queue.isEmpty()) {
                    deck += queue.poll();
                }
            } else {
                deck += queue.poll();
            }
            answer+=deck;
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int[] sizes;
    long answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(sizes);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        sizes = new int[N];

        for (int i = 0; i < N; i++) {
            sizes[i] = Integer.parseInt(rd.readLine());
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
