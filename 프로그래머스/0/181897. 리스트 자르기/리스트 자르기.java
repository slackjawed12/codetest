import java.util.Arrays;
import java.util.ArrayList;
class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        if (n == 1) {
            return Arrays.copyOfRange(num_list, 0, slicer[1]+1);
        } else if (n==2) {
            return Arrays.copyOfRange(num_list, slicer[0], num_list.length);
        } else if (n==3) {
            return Arrays.copyOfRange(num_list, slicer[0], slicer[1]+1);
        } 
        
        ArrayList<Integer> ans = new ArrayList();
        for(int i = slicer[0]; i<num_list.length && i <= slicer[1]; i+= slicer[2]) {
            ans.add(num_list[i]);
        }
        return ans.stream().mapToInt(v->v).toArray();
    }
}