class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        } else {
            String str = String.valueOf(x);
            int i=0;
            int last = str.length()-1;
            while(i<=last/2 && str.charAt(i)==str.charAt(last-i)) {
                i++;
            }
            return i>last/2;
        }
    }
}