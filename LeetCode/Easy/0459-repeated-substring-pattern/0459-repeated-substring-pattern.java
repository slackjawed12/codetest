class Solution {
    public boolean repeatedSubstringPattern(String s) {
        for(int i=1; i<=s.length()/2; i++){
            String temp = s.substring(0, i).repeat(s.length()/i);
            if(temp.equals(s)){
                return true;
            }
        }
        
        return false;
    }
}