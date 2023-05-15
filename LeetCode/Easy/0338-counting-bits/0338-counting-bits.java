class Solution {
    public int[] countBits(int n) {
        int[] answer = new int[n+1];
        answer[0]=0;
        if(n>=1) {
           answer[1]=1; 
        }  
        for(int i=2; i<=n; i++) {
            if(i%2==0){
                answer[i]=answer[i/2];
            } else {
                answer[i]=answer[i/2]+1;
            }
        }
        return answer;
    }
}