import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

class Solution {
    public int[] solve(int[][] table) {
        int[] answer = new int[3];
        int max = -1;
        for (int i = 0; i < table.length; i++) {
            for (int j = 0; j < table[i].length; j++) {
                if (max < table[i][j]) {
                    max = table[i][j];
                    answer[0] = table[i][j];
                    answer[1] = i + 1;
                    answer[2] = j + 1;
                }
            }
        }
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int[][] table;
    int[] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(table);
        output();
    }

    public void input() throws Exception {
        table = new int[9][9];
        for (int i = 0; i < 9; i++) {
            table[i] = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                    .toArray();
        }
    }

    public void output() {
        System.out.println(answer[0]);
        System.out.println(answer[1] + " " + answer[2]);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}