import java.util.*;
import java.util.stream.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        int i=1;
        while(i*i<=n){
            if(n%i==0) {
                answer+=i;
                if(n/i>i) {
                    answer+=n/i;
                }
            }
            i++;
        }
        return answer;
    }
}