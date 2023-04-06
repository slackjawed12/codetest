import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    // pi 배열 구하기 (=longest proper prefix which is suffix 구하기)
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

    public int solve(String S, String P) {
        int[] pi = getPi(P);
        int i = 0, j = 0;   // i : S index, j : P index
        while (i < S.length()) {
            if (S.charAt(i) == P.charAt(j)) {   // match
                i++;
                j++;
                if (j == P.length()) {
                    return 1;
                }
            } else {    // mismatch
                if (j != 0) {
                    j = pi[j - 1];  // pi 배열 값만큼 건너뛰기
                } else {
                    i++;
                }
            }
        }
        return 0;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    String S;
    String P;
    int answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(S, P);
        output();
    }

    public void input() throws Exception {
        S = rd.readLine();
        P = rd.readLine();
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}