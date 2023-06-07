class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0;
        boolean flag = false;
        int cur = 0;
        for(int i=0; i<nums.length; i++){
            if(!flag && nums[i]==1){
                flag=true;
                cur++;
            } else if(nums[i]==1) {
                cur++;
            } else if(nums[i]==0){
                flag=false;
                max=Math.max(max, cur);
                cur=0;
            }
        }
        
        return max=Math.max(max, cur);
    }
}