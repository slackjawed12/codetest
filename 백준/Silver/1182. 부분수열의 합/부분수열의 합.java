import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int S;
    static int answer = 0;

    static void func(int[] array, List<Integer> idx, int last) {
        int sum = 0;
        for (int x : idx) {
            sum += array[x];
        }
        if (sum == S && idx.size()>0) {
            answer++;
        }

        if (idx.size() != N) {
            for (int i = last + 1; i < N; i++) {
                idx.add(i);
                func(array, idx, i);
                idx.remove(idx.size()-1);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] strings = rd.readLine().split(" ");
        N = Integer.parseInt(strings[0]);
        S = Integer.parseInt(strings[1]);
        int[] array = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                .toArray();
        func(array, new ArrayList<>(), -1);
        System.out.println(answer);
    }
}
