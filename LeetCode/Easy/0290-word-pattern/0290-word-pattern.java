class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        
        if(pattern.length()!=words.length) {
            return false;
        }
        
        Map<String, Character> wordMap = new HashMap<>();
        Map<Character, String> charMap = new HashMap<>();
        
        for(int i=0; i<words.length; i++){
            String w = words[i];
            Character c = pattern.charAt(i);
            if(!wordMap.containsKey(w)){
                if(charMap.containsKey(c)) {
                    return false;
                } else {
                    wordMap.put(w, c);
                    charMap.put(c, w);
                }
            } else {
                if(charMap.containsKey(c)) {
                    if(!wordMap.get(w).equals(c)) {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        
        return true;
    }

}