class Solution {
    public List<String> readBinaryWatch(int turnedOn) {
        List<String> answer=new ArrayList<>();
        
        for(int i=0; i<12; i++){
            int hbit = 0;
            int ht=i;
            
            while(ht>0){
                if((ht&1)==1){
                    hbit++;
                }
                
                ht=ht>>1;
            }
            
            for(int j=0; j<60; j++){
                int mbit = 0;
                int mt=j;
            
                while(mt>0){
                    if((mt&1)==1){
                        mbit++;
                    }
                    mt=mt>>1;
                }
                if(hbit+mbit==turnedOn){
                    String display = j/10==0?i+":0"+j:i+":"+j;
                    answer.add(display);
                }
            }
        }
        return answer;
    }
}