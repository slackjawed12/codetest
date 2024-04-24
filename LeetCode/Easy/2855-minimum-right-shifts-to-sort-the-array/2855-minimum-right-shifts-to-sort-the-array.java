class Solution {
    public int minimumRightShifts(List<Integer> nums) {
        int answer = 0;
        int i = 0;
        boolean isFirstIncreasing = true;
        for(i =0; i<nums.size()-1; i++) {
            if(isFirstIncreasing) {
                if(nums.get(i) > nums.get(i+1)) {
                    isFirstIncreasing = false;
                    if(i == nums.size()-2 && nums.get(i+1) > nums.get(0)) {
                        return -1;
                    }
                    answer = 1;
                } 
            } else {
                if(nums.get(i) < nums.get(i+1) && nums.get(i+1) < nums.get(0)) {
                    answer += 1;
                } else {
                    return -1;
                }
            }
        }
        return answer;
    }
}