class Solution {
    public int arrangeCoins(int n) {
        long cur =n;
        int s=0;
        while(cur>0){
            cur-=++s;
        }
        
        return cur<0?s-1:s;
    }
}