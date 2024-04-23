class Solution {
    public String maximumTime(String time) {
       StringBuilder sb = new StringBuilder();
       for(int i =0; i < time.length(); i++) {
            char c = time.charAt(i);
            if(c != '?') {
                sb.append(c);
                continue;
            }
            if(i==0) {
                if (time.charAt(1) == '?' || time.charAt(1) < '4') {
                    sb.append('2');
                } else {
                    sb.append('1');
                }
            } else if (i == 1){
                if (sb.charAt(0) == '2') {
                    sb.append('3');
                } else {
                    sb.append('9');
                }
            } else if (i == 3) {
                    sb.append('5');
            } else if (i== 4) {
                    sb.append('9');
            }
       }
       
       return sb.toString();
    }
}