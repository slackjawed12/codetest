import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] str = rd.readLine().split(" ");
        int points[][] = new int[3][2];
        for (int i = 0; i < str.length; i += 2) {
            points[i / 2][0] = Integer.parseInt(str[i]);
            points[i / 2][1] = Integer.parseInt(str[i + 1]);
        }

        int vectors[][] = {
                {points[1][0] - points[0][0], points[1][1] - points[0][1]},
                {points[2][0] - points[0][0], points[2][1] - points[0][1]},
                {points[2][0] - points[1][0], points[2][1] - points[1][1]}};

        if (vectors[0][0] * vectors[1][1] == vectors[0][1] * vectors[1][0]) {
            System.out.println(-1);
        } else {
            double len[] = new double[3];
            for (int i = 0; i < 3; i++) {
                len[i] = Math.sqrt(vectors[i][0] * vectors[i][0] + vectors[i][1] * vectors[i][1]);
            }
            double maxLen = Math.max(len[0], Math.max(len[1], len[2]));
            double minLen = Math.min(len[0], Math.min(len[1], len[2]));
            System.out.println(2*(maxLen-minLen));
        }
    }
}