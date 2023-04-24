class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> smap = new HashMap<>();
        Map<Character, Character> tmap = new HashMap<>();
        for(int i=0; i<s.length(); i++){
            char cur = s.charAt(i);
            char target = t.charAt(i);
            if(!smap.containsKey(cur)) {
                if(!tmap.containsKey(target)){
                    smap.put(cur, target);
                    tmap.put(target, cur);
                } else {
                    return false;   
                }
            } else {
                if(!tmap.containsKey(target)) {
                    return false;
                } else {
                    if(smap.get(cur)!=target || tmap.get(target)!=cur) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}