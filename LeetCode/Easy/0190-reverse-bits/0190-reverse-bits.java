public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int answer = 0;
        int digit = 0;
        
        while(digit!=32) {
            int bit = (n >> (31-digit)) & 1;
            answer |= bit<<digit++;
        }
        
        return answer;
    }
}