class Solution {
    public int thirdMax(int[] nums) {
        int[] array = new int[3];
        int size = 0;
        for(int i=0; i<nums.length; i++){
            int j=0;
            while(j<size && nums[i]<array[j]){
                j++;
            }
            
            if(j < size && nums[i]==array[j]){
                continue;
            }
            
            size = Math.min(size+1, 3);
            
            int cur=nums[i];
            
            for(int k=j; k<size; k++){
                int temp = cur;
                cur = array[k];
                array[k] = temp;
            }
        }
        
        int answer=0;
        answer = size==3?array[2]:array[0];
        
        return answer;
    }
}