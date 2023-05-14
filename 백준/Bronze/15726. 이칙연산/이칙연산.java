import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

class Solution {
    public int solve(int[] numbers) {
        double answer = Math.max((double) numbers[0] / (double) numbers[1] * (double) numbers[2],
                (double) numbers[0] * (double) numbers[1] / (double) numbers[2]);
        return (int) answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int[] numbers;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(numbers);
        output();
    }

    public void input() throws Exception {
        numbers = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
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