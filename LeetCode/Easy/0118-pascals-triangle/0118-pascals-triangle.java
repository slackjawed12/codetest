import java.util.*;
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(List.of(1));
        for(int i=1; i<numRows; i++){
            List<Integer> row = new ArrayList<>();
            for(int j=0; j<=i; j++){
                if(j==0 || j==i){
                    row.add(1);
                } else {
                    List<Integer> before = ans.get(i-1);
                    row.add(before.get(j-1)+before.get(j));
                }
            }
            ans.add(row);
        }
        
        return ans;
    }
}