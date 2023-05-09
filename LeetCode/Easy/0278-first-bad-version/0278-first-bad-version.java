/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int left, int right) {
        if(left==right) return left;
        long sum = (long)left+(long)right;
        int mid = (int)(sum/2);
        
        return isBadVersion(mid) ? firstBadVersion(left, mid) 
            : firstBadVersion(mid+1, right);
    }
    
    public int firstBadVersion(int n) {
        return firstBadVersion(1, n);
    }
}