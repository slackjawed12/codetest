class Solution {
    public int titleToNumber(String columnTitle) {
        int answer = 0;
        int e = 1;
        int i = columnTitle.length() - 1;
        while(i >= 0) {
            char x = columnTitle.charAt(i--);
            answer += (x - 'A' + 1)*e;
            e*=26;
        }
        
        return answer;
    }
}