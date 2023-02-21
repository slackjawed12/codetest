class Solution {
    public int checkSign(char c){
        return '0'<=c && c <= '9' ? 1 
                : c=='+' ? 1 
                : c=='-' ? -1 : 0;
    }
    
    public boolean isCountable(String s){
        if(s.length() ==0 ) return false;
        else if(s.length() == 1) {
            return isNumber(s.charAt(0));
        } else {
            if(!isNumber(s.charAt(0))) {
                return (s.charAt(0) == '+' || s.charAt(0) =='-') 
                        && isNumber(s.charAt(1));
            } else{
                return true;
            }
        }
    }
    
    public boolean isNumber(char c){
        return '0' <= c && c <='9';
    }
    
    public int myAtoi(String s) {
        int answer =0;
        s = s.trim();
        
        if(!isCountable(s)) return 0;
        
        int sign = checkSign(s.charAt(0));
        
        int i = isNumber(s.charAt(0)) ? 0 : 1;  // first nonzero index
        while(i<s.length() && s.charAt(i) =='0') i++;
        int j = i;  // end index
            
        while(j<s.length() && isNumber(s.charAt(j))) j++;
            
        long digit = 1;
        for(int p = j-1; p>=i; p--){
            if(digit>Integer.MAX_VALUE) {
                return sign == -1?Integer.MIN_VALUE:Integer.MAX_VALUE;
            }
            
            long added = (s.charAt(p)-'0')*digit*sign;
            
            if(answer+added <Integer.MIN_VALUE){
                return Integer.MIN_VALUE;
            }
            if(answer+added>Integer.MAX_VALUE){
                return Integer.MAX_VALUE;
            }
            answer+=added;

            digit*=10;
        }
        
        return answer;
    }
}