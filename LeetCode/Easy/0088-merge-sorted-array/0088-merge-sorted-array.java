import java.util.*;
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] temp = Arrays.copyOfRange(nums1, 0, m+1);
        int i=0, j=0;
        int pos = 0;
        while(i<m && j<n){
            if(temp[i]<=nums2[j]){
                nums1[pos]=temp[i++];
            } else {
                nums1[pos]=nums2[j++];
            }
            pos++;
        }
        
        if(i==m){
            while(j!=n) {
                nums1[pos]=nums2[j++];
                pos++;
            }
        } else {
            while(i!=m){
                nums1[pos] = temp[i++];
                pos++;
            }
        }
    }
}