import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                .toArray();
        int D = Integer.parseInt(rd.readLine());
        int[] added = new int[3];
        added[0] = D / 3600;
        added[1] = (D % 3600) / 60;
        added[2] = D % 3600 % 60;

        int carry = 0;
        for (int i = 2; i >= 0; i--) {
            int result = arr[i] + added[i];
            if (i != 0) {
                arr[i] = (carry + result) % 60;
            } else {
                arr[i] = (carry + result) % 24;
            }
            carry = (carry + result) / 60;
        }

        for (int x : arr) {
            System.out.print(x + " ");
        }
    }
}
