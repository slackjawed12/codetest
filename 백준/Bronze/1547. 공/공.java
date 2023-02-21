import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int M = Integer.parseInt(rd.readLine());
        int start = 1;
        for (int i = 0; i < M; i++) {
            String[] s = rd.readLine().split(" ");
            int x = Integer.parseInt(s[0]);
            int y = Integer.parseInt(s[1]);
            if(x==start) {
                start = y;
            } else if(y==start){
                start = x;
            }
        }

        System.out.println(start);
    }
}