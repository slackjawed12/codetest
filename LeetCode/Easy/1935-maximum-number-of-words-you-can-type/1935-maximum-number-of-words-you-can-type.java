class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        HashSet<Character> brokens = new HashSet();
        for(int i=0; i<brokenLetters.length(); i++) {
            brokens.add(brokenLetters.charAt(i));
        }

        String[] words = text.split(" ");
        int answer =0;
        for(String word : words) {
            boolean hasContain=false;
            for(int i=0; i<word.length(); i++) {
                char c = word.charAt(i);
                if(brokens.contains(c)) {
                    hasContain=true;
                    break;
                }
            }
            answer = hasContain? answer : answer+1;
        }
        return answer;
    }
}