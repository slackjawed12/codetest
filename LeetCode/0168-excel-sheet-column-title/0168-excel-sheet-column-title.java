class Solution {
    public String convertToTitle(int columnNumber) {
        String answer = "";
        while(columnNumber!=0) {
            int r = (columnNumber-1)%26;
            char x = (char)('A' + (char)r);
            answer = x + answer;
            columnNumber = (columnNumber-1)/26;
        }
        
        return answer;
    }
}