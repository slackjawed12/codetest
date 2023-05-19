class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        for(int i=0; i<nums1.length; i++){
            set1.add(nums1[i]);
        }
        
        Set<Integer> interSet = new HashSet<>();
        for(int i=0; i<nums2.length; i++){
            if(set1.contains(nums2[i])) {
                interSet.add(nums2[i]);
            }
        }
        
        int[] answer = new int[interSet.size()];
        int i=0;
        for(int x : interSet) {
            answer[i++] = x;
        }
        return answer;
    }
}