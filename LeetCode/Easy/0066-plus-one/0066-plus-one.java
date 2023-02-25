class Solution {
    public int[] plusOne(int[] digits) {
        digits[digits.length-1]+=1;
        int c=0; // carry
        for(int i=digits.length-1; i>=0; i--){
            if(c+digits[i]>=10){
                digits[i]=digits[i]+c-10;
                c=1;
            } else{
                digits[i]=digits[i]+c;
                c=0;
            }
        }
        
        if(c==1){
            int[] answer = new int[digits.length+1];
            answer[0]=c;
            for(int i=1; i<answer.length; i++){
                answer[i]=digits[i-1];
            }
            return answer;
        } else{
            return digits;
        }
    }
}