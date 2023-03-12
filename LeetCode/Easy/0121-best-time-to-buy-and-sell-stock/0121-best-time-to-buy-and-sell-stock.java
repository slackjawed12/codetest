class Solution {
    public int maxProfit(int[] prices) {
        int low = prices[0];
        int max = 0;
        for(int i=1; i<prices.length; i++){
            if(prices[i] > low) {
                if(prices[i]-low > max){
                    max=prices[i]-low;
                }
            } else {
                low=prices[i];
            }
        }
        return max;
    }
}