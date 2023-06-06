class Solution {
    public int hammingDistance(int x, int y) {
        int a = x ^ y;
        
        int answer = 0;
        while(a!=0){
            answer = (a & 1) == 1 ? answer + 1 : answer;
            a = a >> 1;
        }
        
        return answer;
    }
}