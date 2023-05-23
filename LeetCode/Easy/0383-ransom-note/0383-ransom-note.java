class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] info = new int[26];
        
        for(int i=0; i<ransomNote.length(); i++) {
            info[ransomNote.charAt(i)-'a']++;    
        }
        
        for(int i=0; i<magazine.length(); i++){
            int idx = magazine.charAt(i)-'a';
            info[idx] = info[idx] > 0 ? info[idx]-1 :0;
        }
        
        for(int x : info) {
            if(x!=0) {
                return false;
            }    
        }
        
        return true;
    }
}