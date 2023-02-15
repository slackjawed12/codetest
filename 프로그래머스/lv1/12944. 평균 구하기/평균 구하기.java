import java.util.stream.*;
import java.util.Arrays;
class Solution {
    public double solution(int[] arr) {
        return Arrays.stream(arr).reduce(0, Integer::sum)/(double)arr.length;
    }
}