class Solution {
    public int[] constructRectangle(int area) {
        int[] answer=new int[2];
        for(int i=1; i*i<=area; i++){
            if(area%i==0){
                answer[0]=area/i;
                answer[1]=i;
            }
        }
        
        return answer;
    }
}