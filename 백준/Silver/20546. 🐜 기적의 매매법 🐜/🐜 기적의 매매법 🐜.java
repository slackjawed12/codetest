import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

class Solution {
    public int bnp(int money, int[] chart) {
        int stock = 0;
        for (int i = 0; i < chart.length; i++) {
            int cnt = money / chart[i];
            stock += cnt;
            money -= cnt * chart[i];
        }

        return stock * chart[chart.length - 1] + money;
    }

    public int timing(int money, int[] chart) {
        int stock = 0;
        int inc = 0;
        int dec = 0;

        for (int i = 1; i < chart.length; i++) {
            if (chart[i] > chart[i - 1]) {
                inc++;
                dec = 0;
            }

            if (chart[i] < chart[i - 1]) {
                inc = 0;
                dec++;
            }

            if (inc >= 3) {
                money += stock * chart[i];
                stock = 0;
            }

            if (dec >= 3) {
                int cnt = money / chart[i];
                stock += cnt;
                money -= cnt * chart[i];
            }
        }

        return stock * chart[chart.length - 1] + money;
    }

    public String solve(int money, int[] chart) {
        int b = bnp(money, chart);
        int t = timing(money, chart);
        return b == t ? "SAMESAME" : b > t ? "BNP" : "TIMING";
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int money;
    int[] chart;
    String answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(money, chart);
        output();
    }

    public void input() throws Exception {
        money = Integer.parseInt(rd.readLine());
        chart = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    }

    public void output() throws Exception {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}