import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

class Solution {
    // 재귀 헬퍼 메서드
    // index : 선택한 위치, sum : 현재까지 합
    public void getAllSubsetSum(int[] arr, int r, int index, Long sum, List<Long> result) {
        if (r == 0) {
            result.add(sum);
            return;
        }

        for (int i = index; i < arr.length - r + 1; i++) {
            getAllSubsetSum(arr, r - 1, i + 1, sum + arr[i], result);
        }
    }

    public List<Long> getAllSubsetSum(int[] arr) {
        List<Long> result = new ArrayList<>();
        // 부분집합 원소의 개수 r : 0개부터 배열 전체개수까지
        for (int r = 0; r <= arr.length; r++) {
            getAllSubsetSum(arr, r, 0, 0L, result);
        }
        return result;
    }

    public int binarySearch(Long target, int low, int high, long[] sorted) {
        if (low > high) {
            return low;
        }

        int mid = (low + high) / 2;
        if (sorted[mid] <= target) {
            return binarySearch(target, mid + 1, high, sorted);
        } else {
            return binarySearch(target, low, mid-1, sorted);
        }
    }

    public long solve(int C, int[] weights) {
        long answer = 0;

        // 배열을 앞의 절반과 뒤의 절반으로 나눠서 저장
        int[] head = Arrays.copyOfRange(weights, 0, weights.length / 2);
        int[] tail = Arrays.copyOfRange(weights, weights.length / 2, weights.length);

        // 앞 뒤 각 배열의 모든 부분집합에 대해 합 리스트 구하기
        List<Long> headSum = getAllSubsetSum(head); // O(2^(N/2))
        List<Long> tailSum = getAllSubsetSum(tail); // O(2^(N/2))

        // 뒤 절반은 sort - O(2^(N/2)*log(2^(N/2)))=O(N/2*2^(N/2))
        long[] sorted = tailSum.stream().sorted().mapToLong(Long::longValue).toArray();

        // 앞 배열 각 요소에 대해 + 이분탐색
        // 이분탐색을 통해 처음으로 C보다 큰 값을 갖는 인덱스를 찾아야 함
        // 찾은 인덱스의 직전까지는 C보다 작거나 같음
        // O(2^(N/2)*log(2^(N/2)))=O(N/2*2^(N/2))
        for (Long a : headSum) {
            int result;
            if (C >= a) {
                result = binarySearch(C - a, 0, sorted.length - 1, sorted);
                answer += result;
            }
        }

        return answer;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N;
    int C;
    int[] weights;
    long answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(C, weights);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        C = Integer.parseInt(str[1]);
        weights = Arrays.stream(rd.readLine().split(" "))
                .mapToInt(Integer::parseInt).toArray();
    }

    public void output() {
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}