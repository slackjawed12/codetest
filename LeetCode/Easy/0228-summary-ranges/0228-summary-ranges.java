class Solution {
    public List<String> summaryRanges(int[] nums) {
        if(nums.length == 0) {
            return new ArrayList<>();
        }
        
        List<String> answer = new ArrayList<>();
        int start = nums[0];
        int before = nums[0];
        int current = nums[0];
        String range = "" + start;
        for(int i = 1; i < nums.length; i++){
            current = nums[i];
            if(current != before + 1) {
                if(start!=before){
                    range = range.concat("->" + before);    
                }
                
                answer.add(range);
                start = current;
                range="" + start;
            }
            before = current;
        }
        
        if(start!=before) {
            range = range.concat("->"+before);
        }
        answer.add(range);
        return answer;
    }
}