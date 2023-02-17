import java.util.*;
class Solution {
    public static boolean isPrime(int n) {
        if(n==1) return false;
        int i;
        for(i=2; i*i<=n; i++){
            if(n%i==0) return false;
        }
        return true;
    }
    
    static int answer = 0;
    public static void func(int[] arr, List<Integer> list, int end) {
        if(list.size()==3) {
            int sum = 0;
            for(int idx : list){
                sum+=arr[idx];
            }
            if(isPrime(sum)) {
                answer++;
            } 
        } else {
            for(int i = end+1; i<arr.length-2+list.size(); i++) {
                list.add(i);
                func(arr, list, i);
                list.remove(list.size()-1);
            }
        }
    }
    
    
    public int solution(int[] nums) {
        func(nums, new ArrayList<>(), -1);
        return answer;
    }
}