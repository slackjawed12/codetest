import java.util.*;
import java.util.stream.*;
public class Solution {
    public int[] solution(int []arr) {
        boolean flag = true;
        List<Integer> answer= new ArrayList<>();
        int ex = -1;
        for(int i=0; i<arr.length; i++){
            if(ex != arr[i]){
                ex = arr[i];
                answer.add(ex);
            }
        }
        return answer.stream().mapToInt(x->(int)x).toArray();
    }
}