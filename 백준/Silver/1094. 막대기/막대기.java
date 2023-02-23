import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(rd.readLine());
        int ans = 0;
        while (X != 0) {
            if ((X & 1) == 1) ans++;
            X = X >> 1;
        }
        System.out.println(ans);
    }
}
