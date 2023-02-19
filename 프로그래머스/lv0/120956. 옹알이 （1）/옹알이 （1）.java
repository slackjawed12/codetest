class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] can = {"aya", "ye", "woo", "ma"};
        for(String b : babbling) {
            int i = 0;
            int blen = b.length();
            while(i < blen) {
                int idx = 0;
                for(idx = 0; idx<can.length; idx++) {
                    String c = can[idx];
                    int clen = c.length();
                    int j = 0;
                    while(i+j<blen && j<clen) {
                        if(b.charAt(i+j)!=c.charAt(j)) break;
                        j++;
                    }
                    if(j==clen){
                        i+=j;
                        break;
                    }
                }
                if(idx==can.length) break;
            }
            if(i==blen) answer++;
        }
        return answer;
    }
}