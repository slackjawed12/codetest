class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(int i=0; i<nums1.length; i++){
            map.put(nums1[i], map.getOrDefault(nums1[i], 0)+1);
        }
        
        List<Integer> list = new ArrayList<>();
        for(int i=0; i<nums2.length; i++){
            if (map.containsKey(nums2[i])) {
                list.add(nums2[i]);
                if(map.get(nums2[i])==1) {
                    map.remove(nums2[i]);
                } else {
                    map.put(nums2[i], map.get(nums2[i])-1);   
                }
            }
        }
        return list.stream().mapToInt(x->x).toArray();
    }
}