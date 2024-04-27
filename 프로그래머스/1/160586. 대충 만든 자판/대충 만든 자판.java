import java.util.Arrays;
import java.util.HashMap;
class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        HashMap<Character, Integer> minCount = new HashMap();
        
        for(String key: keymap) {
            for(int i =0; i<key.length(); i++) {
                char k = key.charAt(i);
                int order = minCount.getOrDefault(k, i+1);
                minCount.put(k, Math.min(order, i+1));
            }
        }
        
        int[] answer = new int[targets.length];
        for(int i = 0; i < targets.length; i++) {
            String target = targets[i];
            int sum = 0;
            for(int j=0; j<target.length(); j++) {
                char cur = target.charAt(j);
                int order = minCount.getOrDefault(cur, -1);
                if(order == -1) {
                    sum = -1;
                    break;
                } else {
                    sum += order;
                }
            }
            answer[i] = sum;
        }
        
        return answer;
    }
}