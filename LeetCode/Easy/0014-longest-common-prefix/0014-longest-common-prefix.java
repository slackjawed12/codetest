class Solution {
    public String longestCommonPrefix(String[] strs) {
        String ans = "";
        for(int i=0; i<strs[0].length(); i++){
            int j = 1;
            for(j=1; j<strs.length; j++){
                if(i>=strs[j].length() ||
                   strs[j].charAt(i)!=strs[0].charAt(i)){
                    break;
                }
            }
            if(j==strs.length) ans+=strs[0].charAt(i);
            else break;
        }
        return ans;
    }
}