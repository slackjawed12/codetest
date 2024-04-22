class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        int answer =0;
        for(int i = 0; i<words.length-1; i++) {
            for (int j=i+1; j<words.length; j++) {
                String word = words[i];
                String target = words[j];
                if(target.startsWith(word) && target.endsWith(word)) {
                    answer += 1;
                }
            }
        }

        return answer;
    }
}