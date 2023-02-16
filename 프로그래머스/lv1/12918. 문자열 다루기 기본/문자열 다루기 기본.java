class Solution {
    public boolean solution(String s) {
        try{
            if(s.length() == 4 || s.length() == 6) {
                int x = Integer.parseInt(s);
                return true;
            } else return false;
        } catch (NumberFormatException e) {
            return false;
        }
    }
}