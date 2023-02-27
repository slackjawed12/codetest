class Solution {
    public int mySqrt(int x) {
        int low=0;
        int high=x;
        int mid=0;
        while(low<=high){
            mid=(low+high)/2;
            if((long)mid*mid<x){
                low=mid+1;
            } else if((long)mid*mid==x){
                break;
            } else {
                high=mid-1;
            }
        }
        if(low<=high) return mid;
        else return high;
    }
}