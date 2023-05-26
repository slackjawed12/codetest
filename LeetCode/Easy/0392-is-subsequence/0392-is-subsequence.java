class Solution {
    public boolean isSubsequence(String s, String t) {
        int idx = 0;
        for(int i=0; i<t.length() && idx<s.length(); i++){
            if(t.charAt(i)==s.charAt(idx)){
                idx++;
            }
        }
        return idx==s.length();
    }
}