import java.util.stream.*;
import java.util.*;
class Solution {
    public long solution(long n) {
        char[] arr = String.valueOf(n).toCharArray();
        Arrays.sort(arr);
        return Long.parseLong(new StringBuilder(String.valueOf(arr)).reverse().toString());
    }
}