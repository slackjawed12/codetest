import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String S = rd.readLine();
        int i = Integer.parseInt(rd.readLine());

        System.out.println(S.charAt(i-1));
    }
}