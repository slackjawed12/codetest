import java.io.*;

public class Main{
    public static void main(String[] args)throws Exception{
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(rd.readLine());
        int F = Integer.parseInt(rd.readLine());
        int t = N-N%100;
        int count=0;
        while((t+count)%F!=0){
            count++;
        }
        
        String ans = String.valueOf(count);
        if(ans.length()==1) ans="0"+ans;
        System.out.println(ans);
    }
}