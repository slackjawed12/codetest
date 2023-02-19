import java.util.*;
class Solution {
    public int solution(int[][] dots) {
        List<List<Integer>> vectors = new ArrayList<>();
        for(int i=0; i<dots.length-1; i++){
            for(int j=i+1; j<dots.length; j++){
                List<Integer> vector = new ArrayList<>();
                vector.add(dots[i][0]-dots[j][0]);
                vector.add(dots[i][1]-dots[j][1]);
                vectors.add(vector);
            }
        }
        
        for(int i=0; i<vectors.size()/2-1; i++){
            List<Integer> first = vectors.get(i);
            List<Integer> second = vectors.get(vectors.size()-1-i);
            double m1 = (double)first.get(0)/first.get(1);
            double m2 = (double)second.get(0)/second.get(1);
            if(m1==m2) return 1;
        }
        
        return 0;
    }
}