import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * 21918 - 전구
 */
class Solution {

    public int[] solve(int[][] operation, int[] bulbs) {
        for (int[] op : operation) {
            switch (op[0]) {
                case 1:
                    bulbs[op[1]-1] = op[2];
                    break;
                case 2:
                    for (int i = op[1] - 1; i < op[2]; i++) bulbs[i] ^= 1;
                    break;
                case 3:
                    for (int i = op[1] - 1; i < op[2]; i++) bulbs[i] = 0;
                    break;
                case 4:
                    for (int i = op[1] - 1; i < op[2]; i++) bulbs[i] = 1;
                    break;
                default:
                    break;
            }
        }

        return bulbs;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    int M;
    int[] bulbs;
    int[][] operation;
    int[] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(operation, bulbs);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);
        bulbs = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        operation = new int[M][3];

        for (int i = 0; i < M; i++) {
            operation[i] = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
    }

    public void output() throws Exception {
        for (int j : answer) {
            System.out.print(j + " ");
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}