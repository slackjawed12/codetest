import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

/**
 * 집합의 표현
 */
class Solution {
    public int find(int[] arr, int a) {
        if (arr[a] == a) {
            return a;
        }

        return arr[a] = find(arr, arr[a]);
    }

    public void union(int[] arr, int[] size, int x, int y) {
        x = find(arr, x);
        y = find(arr, y);

        if (x != y) {
            if (size[x] < size[y]) {
                arr[x] = y;
            } else {
                arr[y] = x;
                if (size[x] == size[y]) {
                    size[x]++;
                }
            }
        }
    }

    public List<String> solve(int N, int[][] operation) {
        int[] set = IntStream.range(0, N + 1).toArray();
        int[] size = new int[N + 1];
        Arrays.fill(size, 1);
        List<String> answer = new ArrayList<>();
        for (int[] op : operation) {
            if (op[0] == 1) {
                if (find(set, op[1]) == find(set, op[2])) {
                    answer.add("YES");
                } else {
                    answer.add("NO");
                }
            } else {
                union(set, size, op[1], op[2]);
            }
        }
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int M;
    int[][] operation;
    List<String> answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, operation);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        operation = new int[M][3];
        for (int i = 0; i < M; i++) {
            operation[i] = Arrays.stream(rd.readLine().split(" "))
                    .mapToInt(Integer::parseInt).toArray();
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
