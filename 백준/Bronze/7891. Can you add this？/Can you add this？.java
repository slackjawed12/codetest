//4
//-100 100
//2 3
//0 110101
//-1000000000 1
import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main{
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(rd.readLine());
        List<Integer> answers = new ArrayList<>();
        for(int i=0; i<N; i++) {
            String[] numbers = rd.readLine().split(" ");
            answers.add(Arrays.stream(numbers).mapToInt(Integer::parseInt)
                .reduce(0, Integer::sum));
        }
        
        answers.forEach(System.out::println);
    }
}