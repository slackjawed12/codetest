import java.util.*;
import java.util.stream.*;
class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        HashSet<Character> skipSet = new HashSet<>();
        char[] sarr = s.toCharArray();
        skip.chars().mapToObj(x->(char)x).forEach(skipSet::add);

        for(int idx = 0; idx<sarr.length; idx++){
            List<Character> changer = new ArrayList<>();
            int i =1;
            while(changer.size() < index) {
                char target = (char)((sarr[idx]+i-'a')%26+'a');
                if(!skipSet.contains(target)) {
                    changer.add(target);
                }
                i++;
            }
            sarr[idx]=changer.get(changer.size()-1);
            answer = answer+ String.valueOf(sarr[idx]);
        }
        return answer;
    }
}