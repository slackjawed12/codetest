class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int last = -1;
        for(int i = 0; i < section.length; i++) {
            int cur = section[i];
            if(last < cur){
                last = cur + m - 1;
                answer += 1;
            }
        }
        
        return answer;
    }
}