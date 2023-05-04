class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        
        for(int i=0; i<s.length(); i++){
            sMap.put(s.charAt(i), sMap.getOrDefault(s.charAt(i), 0)+1);
        }
        
        for(int i=0; i<t.length(); i++){
            Character test = t.charAt(i);
            if(sMap.containsKey(test)) {
                if(sMap.get(test) > 0) {
                    sMap.put(t.charAt(i), sMap.get(t.charAt(i))-1);    
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
        
        
        for(Map.Entry<Character, Integer> e : sMap.entrySet()){
            if(e.getValue()!=0){
                return false;
            }    
        }
        return true;
    }
}