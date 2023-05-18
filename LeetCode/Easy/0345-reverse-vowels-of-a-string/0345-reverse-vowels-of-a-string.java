class Solution {
    public boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' ||
            c == 'o' || c == 'u' || c=='A' || c=='E' || c=='I' || c=='O'
            || c=='U';
    }
    
    public String reverseVowels(String s) {
        StringBuilder sb = new StringBuilder();
        List<Character> reverse = new ArrayList<>();
        
        for(int i=s.length()-1; i>=0; i--){
            if(isVowel(s.charAt(i))) {
                reverse.add(s.charAt(i));
            }
        }
        
        int j = 0;
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(isVowel(c)) {
                sb.append(reverse.get(j++));
            } else {
                sb.append(c);
            }
        }
        
        return sb.toString();
    }
}