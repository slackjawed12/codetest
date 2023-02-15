import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(long n) {
        return new StringBuilder(String.valueOf(n)).reverse()
            .toString().chars().map(x->x-'0').toArray();
    }
}