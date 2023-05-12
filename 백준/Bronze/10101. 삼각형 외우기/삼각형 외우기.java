import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution {
    public String solve(int[] angles) {
        String answer = "";
        int[] sorted = Arrays.stream(angles).sorted().toArray();
        if (Arrays.stream(sorted).sum() != 180) {
            answer = "Error";
        } else {
            if (sorted[0] == sorted[1] && sorted[1] == sorted[2]) {
                answer = "Equilateral";
            } else if (sorted[0] == sorted[1] || sorted[1] == sorted[2]) {
                answer = "Isosceles";
            } else {
                answer = "Scalene";
            }
        }
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st; // 입력 많을 때 사용
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int[] angles;
    String answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(angles);
        output();
    }

    public void input() throws Exception {
        angles = new int[3];
        for (int i = 0; i < 3; i++) {
            angles[i]=Integer.parseInt(rd.readLine());
        }
    }


    public void output() throws Exception {
        wr.write(answer);
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
