class Solution {
    public int missingNumber(int[] nums) {
        int answer = 0;
        for(int i=1; i<=nums.length; i++){
            answer^=i;
        }
        for(int i=0; i<nums.length; i++){
            answer^=nums[i];
        }
        return answer;
    }
}