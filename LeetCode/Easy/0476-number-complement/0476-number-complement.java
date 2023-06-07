class Solution {
    public int findComplement(int num) {
        int maxIndex = 0;
        int temp = num;
        while(temp!=0){
            temp = temp >>> 1;
            maxIndex++;
        }
        
        int mask = 0xffffffff;
        int ones = 1;
        while(maxIndex>0){
            mask = ones ^ mask;
            ones = ones << 1;
            maxIndex--;
        }

        return (~num) ^ mask;
    }
}