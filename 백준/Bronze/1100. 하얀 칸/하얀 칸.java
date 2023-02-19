import java.io.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] board = new String[8];
        for(int i=0; i<8 ;i ++){
            board[i]=rd.readLine();
        }
        
        int count =0;
        for(int i=0; i<8; i++){
            for(int j=0 ;j<board[i].length(); j++) {
                if(i%2==0) {
                    if(j%2==0 && board[i].charAt(j)=='F'){
                        count++;
                    }
                } else {
                    if(j%2==1 && board[i].charAt(j)=='F'){
                        count++;
                    }
                }
            }
        }
        
        System.out.println(count);
    }
}