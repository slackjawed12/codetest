import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] getPi(String P) {
        int[] pi = new int[P.length()];
        int x = 0, i = 1;
        while (i < pi.length) {
            if (P.charAt(x) == P.charAt(i)) {
                pi[i++] = ++x;
            } else {
                if (x != 0) {
                    x = pi[x - 1];
                } else {
                    pi[i++] = 0;
                }
            }
        }

        return pi;
    }

    public Answer solve(String S, String P) {
        int[] pi = getPi(P);
        Answer answer = new Answer();
        int i = 0, j = 0;
        while (i < S.length()) {
            if (S.charAt(i) == P.charAt(j)) {
                i++;
                j++;
                if (j == P.length()) {
                    answer.count++;
                    answer.indexes.add(i - j + 1);
                    j = pi[j - 1];
                }
            } else {
                if (j != 0) {
                    j = pi[j - 1];
                } else {
                    i++;
                }
            }
        }
        return answer;
    }
}

class Answer {
    Integer count = 0;
    List<Integer> indexes = new ArrayList<>();
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    String T;
    String P;
    Answer answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(T, P);
        output();
    }

    public void input() throws Exception {
        T = rd.readLine();
        P = rd.readLine();
    }

    public void output() {
        System.out.println(answer.count);
        for (Integer index : answer.indexes) {
            System.out.print(index + " ");
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}