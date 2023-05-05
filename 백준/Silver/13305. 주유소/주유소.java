import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

class Solution {
    public long solve(int N, int[] distance, int[] price) {
        long answer = 0;
        int min = price[0];
        long add = (long) min * distance[0];
        answer += add;
        for (int i = 1; i < distance.length; i++) {
            min = Math.min(min, price[i]);
            add = (long) min * distance[i];
            answer += add;
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int N;
    int[] distance;
    int[] price;
    long answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(N, distance, price);
        output();
    }

    public void input() throws Exception {
        N = Integer.parseInt(rd.readLine());
        distance = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                .toArray();
        price = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
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
