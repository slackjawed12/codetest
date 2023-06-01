class Solution {
    public String addStrings(String num1, String num2) {
        String max = num1.length()>num2.length()?num1:num2;
        String min = num1.length()>num2.length()?num2:num1;
        StringBuilder sb = new StringBuilder();
        int carry=0;
        int i, j;
        for(i=max.length()-1, j=min.length()-1; i>=0 && j>=0; i--, j--){
            int temp = max.charAt(i)-'0'+min.charAt(j)-'0'+carry;
            int number =0;
            if(temp>=10){
                carry=1;
                number=temp-10;
            } else {
                carry =0;
                number=temp;
            }
            sb.insert(0, number);
        }
        
        
        for(; i>=0; i--) {
            int temp = max.charAt(i)-'0'+carry;
            int number =0;
            if(temp>=10){
                carry=1;
                number=temp-10;
            } else {
                carry =0;
                number=temp;
            }
            sb.insert(0, number);
        }
        
        if(carry==1) {
            sb.insert(0, 1);
        }
        
        return sb.toString();
    }
}