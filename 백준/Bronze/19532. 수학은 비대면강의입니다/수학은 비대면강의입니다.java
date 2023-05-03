import java.io.*;
import java.util.Arrays;

class Solution {
    public int[] solve(int[] coeff) {
        int[] answer = new int[2];

        for (int x = -999; x <= 999; x++) {
            for (int y = -999; y <= 999; y++) {
                if (coeff[0] * x + coeff[1] * y == coeff[2] &&
                        coeff[3] * x + coeff[4] * y == coeff[5]) {
                    answer[0] = x;
                    answer[1] = y;
                    return answer;
                }
            }
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int[] coeff;
    int[] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(coeff);
        output();
    }

    public void input() throws Exception {
        coeff = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                .toArray();
        answer = new int[2];
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
