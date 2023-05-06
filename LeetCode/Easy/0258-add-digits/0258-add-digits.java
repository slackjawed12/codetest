class Solution {
    public int addDigits(int num) {
        while(num/10!=0){
            int x = num;
            int y = 0;
            while(x!=0){
                y+=x%10;
                x/=10;
            }
            
            num=y;
        }
        
        return num;
    }
}