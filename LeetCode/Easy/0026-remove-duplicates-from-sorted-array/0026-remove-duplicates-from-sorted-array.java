class Solution {
    public int removeDuplicates(int[] nums) {
        int cur =0;
        int ex = -200;
        for(int i=0; i<nums.length; i++){
            if(nums[i]!=ex) {
                ex=nums[i];
                nums[cur]=nums[i];
                cur++;
            }
        }
        
        return cur;
    }
}