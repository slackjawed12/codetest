class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        int maxlen = 0;
        int minlen = 0;
        for(int i=0; i<sizes.length; i++){
            int l = Math.max(sizes[i][0], sizes[i][1]);
            int s = Math.min(sizes[i][0], sizes[i][1]);
            if(maxlen<l) {
                maxlen=l;
            }
            if(minlen<s) {
                minlen=s;
            }
        }
        return maxlen*minlen;
    }
}