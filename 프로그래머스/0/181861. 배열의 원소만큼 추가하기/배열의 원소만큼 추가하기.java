class Solution {
    public int[] solution(int[] arr) {
        int len = 0;
        for(int elem : arr) {
            len += elem;
        }
        
        int[] answer = new int[len];
        int last = 0;
        for(int i = 0; i<arr.length; i++) {
            for (int j=0; j<arr[i]; j++) {
                answer[last+j]=arr[i];
            }
            last += arr[i];
        }
        
        return answer;
    }
}