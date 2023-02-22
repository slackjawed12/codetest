import java.util.*;

class Solution {
    
    public boolean isPair(char o, char c){
        switch(c){
            case ')':
                return o=='(';
            case ']':
                return o=='[';
            case '}':
                return o=='{';
            default:
                return false;
        }
    }
    
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c=='(' || c=='[' || c=='{') {
                st.push(c);
            } else if(!st.empty()) {
                char open = st.peek();
                if(isPair(open, c)) st.pop();
                else st.push(c);
            } else {
                return false;
            }
        }
        
        if(st.size()==0) return true;
        else return false;
    }
}