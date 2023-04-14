class Solution {
    public int majorityElement(int[] nums) {
        int major = nums[0];
        int count = 1;
        for(int i=1; i<nums.length; i++) {
            int cur = nums[i];
            
            if(major==cur) {
                count++;
            } else if(count==0) {
                major=cur;
                count++;
            } else {
                count--;
            }
        }
        
        return major;
    }
}