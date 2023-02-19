import java.io.*;

public class Main{
    public static void main(String[] args)throws Exception{
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(rd.readLine());
        String[] answer = new String[N];
        for(int i=0 ;i<N; i++){
            String[] arr = rd.readLine().split(" ");
            int x = 0;
            int a = Integer.parseInt(arr[0]);
            int b = Integer.parseInt(arr[1]);
            int c = Integer.parseInt(arr[2]);
            if(a<=b && b<= c || a>= b && b>=c){
                answer[i]="Ordered";
            } else {
                answer[i]="Unordered";
            }
        }
        
        System.out.println("Gnomes:");
        for(int i=0; i<N; i++){
            System.out.println(answer[i]);
        }
    }
}