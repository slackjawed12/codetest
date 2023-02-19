import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String str="";
        List<Integer> answers = new ArrayList<>();
        while(!(str=rd.readLine()).equals("0")) {
            int temp=1;
            for(int i=0;i<str.length();i++){
                if(str.charAt(i)=='1'){
                    temp+=2;
                } else if(str.charAt(i)=='0'){
                    temp+=4;
                } else {
                    temp+=3;
                }
                temp++;
            }
            answers.add(temp);
        }
        answers.forEach(System.out::println);
    }
}