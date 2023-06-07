class Solution {
    public String licenseKeyFormatting(String s, int k) {
        StringBuilder sb = new StringBuilder();
        Stack<String> bucket = new Stack<>();
        Stack<Character> st = new Stack<>();
        
        for(int i=s.length()-1; i>=0; i--){
            char cur = s.charAt(i);
            if('a'<= cur && cur<='z'){
                cur-=32;
            } 
            
            if(cur != '-'){
                st.push(cur);
            }
            
            if(st.size()==k){
                StringBuilder temp = new StringBuilder();
                while(!st.isEmpty()){
                    temp.append(st.pop());
                }
                bucket.push(temp.toString());
            }
        }
        
        StringBuilder temp = new StringBuilder();
        while(!st.isEmpty()){
            temp.append(st.pop());
        }
        
        if(temp.length()>0){
            bucket.push(temp.toString());   
        }
        
        while(!bucket.isEmpty()){
            sb.append("-"+bucket.pop());
        }

        if(sb.toString().length() > 0) {
            return sb.toString().substring(1);   
        } else {
            return sb.toString();
        }
    }
}