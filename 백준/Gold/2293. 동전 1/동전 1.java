import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] str = rd.readLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int k = Integer.parseInt(str[1]);
        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            list.add(Integer.parseInt(rd.readLine()));
        }

        int[] dp = new int[k + 1];
        dp[0] = 0;

        for (int i = 0; i < list.size(); i++) {
            int val = list.get(i);
            for (int j = 1; j <= k; j++) {
                if (j == val) dp[j]++;
                if(j>val) {
                    dp[j] += dp[j - val];
                }
            }
        }

        System.out.println(dp[k]);
    }
}