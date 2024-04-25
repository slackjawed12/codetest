class Solution {
    public int minimumPushes(String word) {
        return word.length() + Math.max(word.length()-8, 0) + Math.max(word.length() - 16, 0) + Math.max(word.length()-24,0);
    }
}