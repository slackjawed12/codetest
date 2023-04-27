import java.io.*;

class Solution {
    public int[] solve(int C) {
        int[] answer = new int[4];
        int[] arr = {25, 10, 5, 1};

        for (int i = 0; i < 4; i++) {
            answer[i]=C/arr[i];
            C%=arr[i];
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int T;
    int C;
    int[][] answer;

    public void submit() throws Exception {
        T = Integer.parseInt(rd.readLine());
        answer=new int[T][4];
        for (int i = 0; i < T; i++) {
            input();
            answer[i] = new Solution().solve(C);
        }
        output();
    }

    public void input() throws Exception {
        C = Integer.parseInt(rd.readLine());
    }

    public void output() throws Exception {
        for (int[] a : answer) {
            for (int j : a) {
                wr.write(j + " ");
            }
            wr.write("\n");
        }
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}