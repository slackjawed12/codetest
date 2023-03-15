import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int[] total = new int[2];
        for (int i = 0; i < 2; i++) {
            total[i] = Arrays.stream(rd.readLine().split(" "))
                    .map(Integer::parseInt).reduce(0, Integer::sum);
        }
        System.out.println(Math.max(total[0], total[1]));
    }
}
