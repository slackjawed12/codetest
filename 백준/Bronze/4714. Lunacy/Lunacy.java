import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        float f = 0f;
        ArrayList<Float> weight = new ArrayList<>();
        while ((f = Float.parseFloat(rd.readLine())) > 0) {
            weight.add(f);
        }

        for (float x : weight) {
            System.out.print("Objects weighing ");
            System.out.printf("%.2f", x);
            System.out.print(" on Earth will weigh ");
            System.out.printf("%.2f", x*0.167);
            System.out.println(" on the moon.");
        }
    }
}