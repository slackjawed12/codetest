class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        
        for(int i=0; i<nums.length; i++){
            int cur = nums[i];
            List<Integer> list = map.getOrDefault(cur, new ArrayList<>());
            list.add(i);
            map.put(nums[i], list);
        }
        
        for(Map.Entry<Integer, List<Integer>> e : map.entrySet()){
            List<Integer> list = e.getValue();
            for(int i=0; i<list.size()-1; i++){
                if(list.get(i+1)-list.get(i)<=k){
                    return true;
                }
            }
        }
        
        return false;
    }
}