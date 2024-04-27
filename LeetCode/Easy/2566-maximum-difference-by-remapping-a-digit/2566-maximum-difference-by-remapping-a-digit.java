class Solution {
    public int minMaxDifference(int num) {
        HashSet<Integer> digits = new HashSet();
        int temp = num;
        while (temp > 0) {
            digits.add(temp % 10);
            temp /= 10;
        }
        
        SortedSet<String> set = new TreeSet();
        for(int d : digits) {
            String origin = Integer.toString(num);
            String max = origin.replace(Integer.toString(d), "9");
            String min = origin.replace(Integer.toString(d), "0");
            set.add(max);
            set.add(min);
        }
        int answer = Integer.parseInt(set.last()) - Integer.parseInt(set.first());
        return answer;
    }
}