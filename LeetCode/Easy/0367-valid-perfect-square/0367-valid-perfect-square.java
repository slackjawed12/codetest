class Solution {
    public boolean isPerfectSquare(int num) {
        int left = 1;
        int right = num;
        long mid = (left+(long)right)/2;
        while(left<=right) {
            long temp = mid*mid;
            if(temp==(long)num) {
                return true;
            } else if(temp>(long)num) {
                right = (int)(mid - 1);
            } else {
                left = (int)(mid + 1);
            }
            
            mid=(left+(long)right)/2;
        }
        
        return false;
    }
}