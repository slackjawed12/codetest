import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        final int total = Arrays.stream(rd.readLine().split(" "))
                .mapToInt(Integer::parseInt).reduce(1, (x,y)->x*y);
        int[] arr= Arrays.stream(rd.readLine().split(" "))
                .mapToInt(Integer::parseInt).map(x->x-total)
                .toArray();
        for(int e : arr) {
            System.out.print(e+" ");
        }
    }
}