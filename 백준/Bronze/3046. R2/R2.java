import java.io.*;
class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] x = rd.readLine().split(" ");
        int a = Integer.parseInt(x[0]);
        int b= Integer.parseInt(x[1]);
        
        System.out.println(2*b-a);
    }
}