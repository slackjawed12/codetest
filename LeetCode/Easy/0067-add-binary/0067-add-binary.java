class Solution {
    public String addBinary(String a, String b) {
        String answer="";
        if(a.length()<b.length()) {
            a = "0".repeat(b.length()-a.length())+a;
        } else {
            b="0".repeat(a.length()-b.length())+b;
        }
        
        int carry=0;
        for(int i=a.length()-1; i>=0; i--){
            int val = a.charAt(i)-'0'+b.charAt(i)-'0'+carry;
            if(val>=2) {
                val-=2;
                carry=1;
            } else {
                carry=0;
            }
            answer=val+answer;
        }
        
        if(carry==1) answer=carry+answer;
        return answer;
    }
}