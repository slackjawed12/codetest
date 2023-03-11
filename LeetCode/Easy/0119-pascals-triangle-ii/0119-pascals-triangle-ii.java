class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> ans = new ArrayList<>();
        long mul =1;
        for(int i=1; i<=rowIndex+1; i++){
            ans.add((int)mul);
            mul*=(rowIndex-i+1);
            mul/=i;
        }
        
        return ans;
    }
}