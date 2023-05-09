import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.time.LocalTime;
import java.util.Arrays;


class Solution {
    public int[][] solve(int[][] time) {
        int[][] answer = new int[3][3];
        for (int i = 0; i < 3; i++) {
            int[] info = time[i];
            LocalTime t = LocalTime.of(info[3], info[4], info[5]);
            t = t.minusHours(info[0]);
            t= t.minusMinutes(info[1]);
            t= t.minusSeconds(info[2]);
            answer[i][0]=t.getHour();
            answer[i][1]=t.getMinute();
            answer[i][2]=t.getSecond();
        }
        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    int[][] time;
    int[][] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(time);
        output();
    }

    public void input() throws Exception {
        time=new int[3][6];
        for (int i = 0; i < 3; i++) {
            time[i]= Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt)
                    .toArray();
        }
    }


    public void output() throws Exception {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                wr.write(answer[i][j]+" ");
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