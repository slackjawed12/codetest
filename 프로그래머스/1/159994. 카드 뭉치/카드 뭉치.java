import java.util.ArrayDeque;
import java.util.Deque;
class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        int i=0;
        int j=0;
        int k=0;
        for(i=0; i<goal.length; i++) {
            String one = j == cards1.length ? null : cards1[j];
            String two = k == cards2.length ? null : cards2[k];
            String cur = goal[i];
            
            if(cur.equals(one)) {
                j++;
            } else if (cur.equals(two)) {
                k++;
            } else {
                return "No";
            }
        }
        
        return "Yes";
    }
}