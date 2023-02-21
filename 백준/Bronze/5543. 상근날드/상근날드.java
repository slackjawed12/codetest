import java.io.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int[] arr =new int[5];
        for(int i=0; i<5; i++){
            arr[i]=Integer.parseInt(rd.readLine());
        }
        
        int minBurger = arr[0];
        int minBeverage = arr[3]<arr[4]?arr[3]:arr[4];
        for(int i=0;i<3; i++){
            if(minBurger>arr[i]) minBurger=arr[i];
        }
        System.out.println(minBurger+minBeverage-50);
    }
}