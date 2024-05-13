class Solution {
    public int[] solution(String[] wallpaper) {
        int luy = wallpaper[0].length();
        int lux = wallpaper.length;
        int rdx = 0;
        int rdy = 0;
        for(int i =0; i<wallpaper.length; i++) {
            for(int j =0; j<wallpaper[i].length(); j++) {
                char cur = wallpaper[i].charAt(j);
                if(cur == '#') {
                    luy = Math.min(j, luy);
                    lux = Math.min(i, lux);
                    rdx = Math.max(i, rdx);
                    rdy = Math.max(j, rdy);
                }
            }
        }
        int[] result = {lux, luy, rdx+1, rdy+1};
        return result;
    }
}