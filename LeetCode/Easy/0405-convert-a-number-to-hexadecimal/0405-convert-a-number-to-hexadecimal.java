class Solution {
    public String toHex(int num) {
        if(num==0){
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        int cnt=0;
        int temp = 0;
        while(num!=0){
            temp=num & 0x0000000f;
            sb.insert(0, temp>=10?String.valueOf((char)('a'+temp-10)):temp);
            num = num >>> 4;
        }
        
        return sb.toString();
    }
}