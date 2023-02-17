import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        HashSet<Integer> set = new HashSet<>();
        for(int i=0; i<win_nums.length; i++){
            set.add(win_nums[i]);
        }        
        
        long maxResult = Arrays.stream(lottos).filter(x->x==0 || set.contains(x))
            .count();
        long minResult = Arrays.stream(lottos).filter(x->x!=0 && set.contains(x))
            .count();
        
        maxResult = 7-maxResult>=6? 6 : 7-maxResult;
        minResult = 7-minResult>=6? 6 : 7-minResult;
        answer[0]=(int)(maxResult);
        answer[1]=(int)(minResult);
        return answer;
    }
}