class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int i=0; i<nums.length; i++){
            set.add(nums[i]);
        }
        
        List<Integer> answer = new ArrayList<>();
        for(int i=1; i<=nums.length; i++){
            if(!set.contains(i)){
                answer.add(i);
            }
        }
        return answer;
    }
}