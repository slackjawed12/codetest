import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

class Solution {
    public int[] solve(int N, int[] array) {
        int[] answer = new int[N];
        Deque<Integer> stack = new ArrayDeque<>();

        stack.push(array[N - 1]);
        answer[N - 1] = -1;

        for (int i = N - 2; i >= 0; i--) {
            int num = array[i];

            while (!stack.isEmpty() && num >= stack.peek()) {
                stack.pop();
            }

            if (stack.isEmpty()) {
                answer[i] = -1;
            } else {
                answer[i] = stack.peek();
            }
            stack.push(num);
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int[] array;
    int[] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, array);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        array = Arrays.stream(rd.readLine().split(" "))
                .mapToInt(Integer::parseInt).toArray();
    }

    public void output() throws Exception {
        for (int i : answer) {
            wr.write(i + " ");
        }
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}