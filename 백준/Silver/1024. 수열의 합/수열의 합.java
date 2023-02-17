import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.stream.LongStream;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] x = rd.readLine().split(" ");
        long N = Long.parseLong(x[0]);
        long L = Long.parseLong(x[1]);
        long first = -1;
        long a;
        long b = 2 * N - L * (L - 1);
        while (L <= 100 && b >= 0) {
            a = 2 * L;
            b = 2 * N - L * (L - 1);

            if (b % a == 0) {
                first = b / a;
                break;
            }

            L++;
        }

        if (first == -1) {
            System.out.println(-1);
        } else {
            LongStream.range(first, first + L).forEach(p -> System.out.print(p + " "));
        }
    }
}