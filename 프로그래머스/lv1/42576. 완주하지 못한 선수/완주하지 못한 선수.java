import java.util.*;
import java.util.stream.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<>();
        Arrays.stream(completion).forEach(x->{
            map.put(x, map.getOrDefault(x, 0)+1);
        });
        
        for(String name:participant){
            if(map.containsKey(name)){
                if(map.get(name)==1){
                    map.remove(name);
                } else {
                    map.put(name, map.get(name)-1);
                }
            } else {
                answer = name;
                break;
            }
        }
        return answer;
    }
}