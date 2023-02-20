import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static char[] move(String direction, char[] curPos) {
        char[] next = Arrays.copyOf(curPos, 2);
        switch (direction) {
            case "R" :
                next[0] = (char) (curPos[0] + 1);
                break;
            case "L" : 
                next[0] = (char) (curPos[0] - 1);
                break;
            case "B" :
                next[1] = (char) (curPos[1] - 1);
                break;
            case "T" : 
                next[1] = (char) (curPos[1] + 1);
                break;
            case "RT" :
                next[0] = (char) (curPos[0] + 1);
                next[1] = (char) (curPos[1] + 1);
                break;
            case "LT" : 
                next[0] = (char) (curPos[0] - 1);
                next[1] = (char) (curPos[1] + 1);
                break;
            case "RB" : 
                next[0] = (char) (curPos[0] + 1);
                next[1] = (char) (curPos[1] - 1);
                break;
            case "LB" : 
                next[0] = (char) (curPos[0] - 1);
                next[1] = (char) (curPos[1] - 1);
                break;
            default :
                break;
        }
        return next;
    }
    public static boolean isInBound(char[] pos) {
        return 'A'<=pos[0] && pos[0]<='H' && '1'<=pos[1] && pos[1]<='8';
    }
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        char kingPos[] = new char[2];
        char stonePos[] = new char[2];
        String[] strings = rd.readLine().split(" ");
        kingPos[0] = strings[0].charAt(0);
        kingPos[1] = strings[0].charAt(1);
        stonePos[0] = strings[1].charAt(0);
        stonePos[1] = strings[1].charAt(1);
        int N = Integer.parseInt(strings[2]);

        for (int i = 0; i < N; i++) {
            String dir = rd.readLine();
            char kingNext[] = move(dir, kingPos);
            char stoneNext[] = Arrays.copyOf(stonePos, 2);
            if (stonePos[0] == kingNext[0] && stonePos[1] == kingNext[1]) {
                stoneNext = move(dir, stonePos);
            }
            if(isInBound(stoneNext) && isInBound(kingNext)) {
                kingPos = Arrays.copyOf(kingNext, 2);
                stonePos = Arrays.copyOf(stoneNext, 2);
            }
        }

        System.out.println(String.valueOf(kingPos));
        System.out.println(String.valueOf(stonePos));
    }
}