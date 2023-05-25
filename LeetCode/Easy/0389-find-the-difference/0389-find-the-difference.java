class Solution {
    public char findTheDifference(String s, String t) {
        int[] info = new int[26];
        
        for(int i=0; i<s.length(); i++) {
            info[s.charAt(i)-'a']++;
        }
        
        for(int i=0; i<t.length(); i++) {
            info[t.charAt(i)-'a']--;
        }
        
        char answer='a';
        for(int i=0; i<26; i++){
            if(info[i]==-1){
                answer=(char)('a'+i);
            }
        }
        return answer;
    }
}