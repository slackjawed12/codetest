import java.util.*;
class Solution {
    public int solution(int[][] lines) {
        List<List<Integer>> dup = new ArrayList<>();
        int idx=0;
        for(int i=0; i<lines.length-1; i++){
            for(int j=i+1; j<lines.length; j++){
                int s = lines[i][0]>lines[j][0]?lines[i][0]:lines[j][0];
                int e = lines[i][1]>lines[j][1]?lines[j][1]:lines[i][1];
                if(e > s) {
                    List<Integer> l = new ArrayList<Integer>();
                    l.add(s);
                    l.add(e);
                    dup.add(l);
                }
                idx++;
            }
        }
        dup.sort((o1, o2) -> o1.get(0)!=o2.get(0) ? o1.get(0)-o2.get(0)
                            : o1.get(1)-o2.get(1));

        int answer =0;
        if(dup.size()==0) return 0;
        else {
            int low = dup.get(0).get(0);
            int high = dup.get(0).get(1);
            answer+=high-low;
            for(int i=1 ;i<dup.size(); i++){
                int p = dup.get(i).get(0) > high?dup.get(i).get(0) : high;
                answer+=dup.get(i).get(1)-p;
                high=dup.get(i).get(1);
            }
        }
        
        return answer;
    }
}