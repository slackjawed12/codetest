import java.util.*;

class Solution {
    public int romanToInt(String s) {
        int ans = 0;
        int i=0;
        HashMap<Character, Integer> map = new HashMap<>();
        map.put('M', 1000);
        map.put('D', 500);
        map.put('C', 100);
        map.put('L', 50);
        map.put('X', 10);
        map.put('V', 5);
        map.put('I', 1);
        for(i=0; i<s.length()-1; i++){
            char x = s.charAt(i);
            char n = s.charAt(i+1);
            if(x=='C' && (n=='D'||n=='M')) ans-=map.get(x);
            else if(x=='X' && (n=='L'||n=='C')) ans-=map.get(x);
            else if (x=='I' && (n=='V'||n=='X')) ans-=map.get(x);
            else ans+=map.get(x);
        }
        ans+=map.get(s.charAt(i));
        return ans;
    }
}