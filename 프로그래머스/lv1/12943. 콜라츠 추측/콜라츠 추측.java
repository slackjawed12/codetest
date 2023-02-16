class Solution {
    static int cnt = 0;
    public int solution(int num) {
        long t=num;
        int cnt=0;
        while(t!=1 && cnt<=500){
            if(t%2==0){
                t/=2;
            } else {
                t=t*3+1;
            }
            cnt++;
        }
        
        return cnt>500? -1 : cnt;
    }
}