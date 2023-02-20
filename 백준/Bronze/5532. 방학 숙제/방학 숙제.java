import java.io.*;

public class Main{
    public static void main(String[] args)throws Exception{
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int L = Integer.parseInt(rd.readLine());
        int A = Integer.parseInt(rd.readLine());
        int B = Integer.parseInt(rd.readLine());
        int C = Integer.parseInt(rd.readLine());
        int D = Integer.parseInt(rd.readLine());
        int kor = A%C==0?A/C:A/C+1;
        int math = B%D==0?B/D:B/D+1;
        if(kor<=math){
            System.out.println(L-math);
        } else{
            System.out.println(L-kor);
        }
    }
}