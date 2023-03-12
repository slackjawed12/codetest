class Solution {    
    public boolean isPalindrome(String s) {
        List<Character> list = new ArrayList<>();
        for(int i=0; i<s.length(); i++){
            char x = s.charAt(i);
            if('A'<= x && x<='Z'){
                list.add((char)(x-'A'+'a'));
            } else if ('a'<=x && x<='z' || '0'<=x && x<='9') {
                list.add(x);
            }
        }
        for(int i=0; i<list.size()/2; i++){
            if(list.get(i)!=list.get(list.size()-1-i)) {
                return false;
            }
        }
        return true;
    }
}