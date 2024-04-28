import java.util.HashMap;
import java.util.ArrayList;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        HashMap<String, Integer> scores = new HashMap();
        for(int i=0; i<name.length; i++) {
            scores.put(name[i], yearning[i]);
        }
        ArrayList<Integer> answer = new ArrayList();
        for(String[] picture: photo) {
            int score = 0;
            for(String person: picture) {
                score += scores.getOrDefault(person, 0);
            }
            answer.add(score);
        }
        
        return answer.stream().mapToInt(v->v).toArray();
    }
}