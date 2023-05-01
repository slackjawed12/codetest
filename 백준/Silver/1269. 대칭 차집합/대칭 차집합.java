import java.io.*;
import java.util.Arrays;
import java.util.HashSet;

class Solution {
    public int solve(int[] A, int[] B) {
        HashSet<Integer> setA = new HashSet<>();
        HashSet<Integer> setB = new HashSet<>();

        Arrays.stream(A).forEach(setA::add);
        Arrays.stream(B).forEach(setB::add);

        int onlyA = 0;
        for (Integer x : setA) {
            if (!setB.contains(x)) {
                onlyA++;
            }
        }

        return onlyA + setB.size()-(setA.size()-onlyA);
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int Na;
    int Nb;
    int[] A;
    int[] B;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(A, B);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        Na = Integer.parseInt(str[0]);
        Nb = Integer.parseInt(str[1]);

        A = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        B = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    }

    public void output() throws Exception {
        wr.write(String.valueOf(answer));
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
