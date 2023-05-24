import java.util.TreeMap;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        TreeMap<Integer, Integer> q = new TreeMap<>();
        
        for(int i=0; i<operations.length; i++){
            String[] op = operations[i].split(" ");
            int val = Integer.parseInt(op[1]);
            if(op[0].charAt(0)=='I') {
                q.put(val, q.getOrDefault(val, 0)+1);
            } else if(!q.isEmpty()) {   // q가 비어있지 않으면 제거 연산 실행
                if(Integer.parseInt(op[1])==-1) {   // 최솟값 제거
                    int key = q.firstEntry().getKey();
                    int count = q.firstEntry().getValue();
                    if(count==1) {
                        q.pollFirstEntry();
                    } else {
                        q.put(key, count-1);   
                    }
                } else {    // 최댓값 제거
                    int key = q.lastEntry().getKey();
                    int count = q.lastEntry().getValue();
                    if(count==1) {
                        q.pollLastEntry();
                    } else {
                        q.put(key, count-1);   
                    }
                }
            }
        }
        
        if(q.isEmpty()){
            answer[0]=0;
            answer[1]=0;
        } else {
            answer[0] = q.lastKey();
            answer[1] = q.firstKey();
        }
        
        return answer;
    }
}