class Solution {
    public boolean isHappy(int n) {
        Map<Integer, Boolean> map = new HashMap<>();
        map.put(n, true);
        while(n!=1){
            int next = 0;
            int cur = n;
            while(cur!=0) {
                next += (cur%10)*(cur%10);
                cur/=10;
            }
            if(map.containsKey(next)) {
                return false;
            }
            n = next;
            map.put(n, true);
        }
        return true;
    }
}