class Solution {
    public String solution(String s, int n) {
        String answer = "";

        for (int i = 0; i < s.length(); i++) {
            int ch = s.charAt(i);
            answer += 'a' <= ch && ch <= 'z' ? (char) ((ch-'a'+n)%26+'a')
                    : 'A' <= ch && ch <= 'Z' ? (char) ((ch-'A'+n)%26+'A')
                    : (char)ch;
        }
        
        return answer;
    }
}