class Solution {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int rem = k;
        int answer = 0;
        int[] arr = {numOnes, numZeros, numNegOnes};
        for(int i=0; i<arr.length; i++) {
            int take = Math.min(rem, arr[i]);
            answer += i == 0? take : i == 1 ? 0 : -take;
            rem -= take;
        }
        return answer;
    }
}