import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * 광고
 */
class Solution {
    public int[] getPi(String str) {
        int[] pi = new int[str.length()];
        int x = 0, i = 1;
        while (i != str.length()) {
            if (str.charAt(x) == str.charAt(i)) {
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

    public int solve(int L, String str) {
        return L - getPi(str)[str.length() - 1];
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int L;
    String str;
    int answer;
    
    public void submit() throws Exception {
        input();
        answer = new Solution().solve(L, str);
        output();
    }
    
    public void input() throws Exception {
        L = Integer.parseInt(rd.readLine());
        str = rd.readLine();
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}