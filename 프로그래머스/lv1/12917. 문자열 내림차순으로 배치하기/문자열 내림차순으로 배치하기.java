import java.util.*;
class Solution {
    public String solution(String s) {
        char[] c = s.toCharArray();
        Arrays.sort(c);
        
        return new StringBuilder(String.valueOf(c)).reverse().toString();
    }
}