import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    public double getScore(String grade) {
        if (grade.equals("F")) {
            return 0;
        } else {
            double score = 0;
            if (grade.charAt(1) == '+') {
                score += 0.5;
            }
            char a = grade.charAt(0);
            score += a == 'A' ? 4 : a == 'B' ? 3 : a == 'C' ? 2 : a == 'D' ? 1 : 0;
            return score;
        }
    }

    public double solve(String[][] info) {
        double creditSum = 0;
        double total = 0;
        for (int i = 0; i < info.length; i++) {
            String grade = info[i][1];
            double credit = Double.parseDouble(info[i][0]);
            if (!grade.equals("P")) {
                double score = getScore(grade);
                total += score * credit;
                creditSum += credit;
            }
        }
        return total / creditSum;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    String[][] info;
    double answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(info);
        output();
    }

    public void input() throws Exception {
        info = new String[20][2];
        for (int i = 0; i < 20; i++) {
            String[] str = rd.readLine().split(" ");
            info[i][0] = str[1];
            info[i][1] = str[2];
        }
    }

    public void output() {
        System.out.printf("%.6f", answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}