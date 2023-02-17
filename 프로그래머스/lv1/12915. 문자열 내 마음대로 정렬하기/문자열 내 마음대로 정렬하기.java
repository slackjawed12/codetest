import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
        List<String> st = new ArrayList<>();
        for(int i=0; i<strings.length; i++){
            st.add(strings[i]);
        }
        st.sort((s1,s2)->{
            return s1.charAt(n)!=s2.charAt(n)
                    ? s1.charAt(n)-s2.charAt(n)
                    : s1.compareTo(s2);
        });
        System.out.println(st);
        String[] answer=new String[st.size()];
        for(int i =0; i<st.size(); i++){
            answer[i]=st.get(i);
        }
        return answer;
        
    }
}