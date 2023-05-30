class Solution {
    public int longestPalindrome(String s) {
        Map<Character, Integer> map = new HashMap<>();
        for(int i=0; i<s.length(); i++){
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0)+1);
        }
        
        int answer =0;
        boolean isOdd=false;
        for(Map.Entry<Character, Integer> e : map.entrySet()){
            if(e.getValue()%2!=0){
                if(!isOdd){
                    answer+=1;    
                    isOdd = true;
                }
                answer+=e.getValue()-1;
            } else {
                answer+=e.getValue();
            }
        }
        
        return answer;
    }
}