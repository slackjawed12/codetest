class Solution {
    public int solution(int n) {
        int answer = 0;
        int t = n;
        String x = "";
        while(t!=0) {
            x+=t%3;
            t/=3;
        }
        
        int digit=1;
        for(int i=x.length()-1; i>=0; i--)
        {
            int a = x.charAt(i)-'0';
            answer+=a*digit;
            digit*=3;
        }
        return answer;
    }
}