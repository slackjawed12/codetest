import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static int N;

    // n개중 r개 뽑는 combi 함수 - depth 0 시작
    // 뽑을때마다 N을 하나 줄인다.
    public static void combi(List<Integer> l, int depth, int n, int r) {
        if (N > 0) {
            if (depth < r) {
                for (int i = r - depth - 1; i <= n - 1; i++) {
                    l.add(i);
                    combi(l, depth + 1, i, r);
                    l.remove(l.size() - 1);
                }
            } else {
                if(--N == 0) l.forEach(System.out::print);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(rd.readLine());
        for (int i = 1; i <= 10; i++) {
            // 10개 중 1개 뽑는 조합 ~ 10개 뽑는 조합을 구한다.
            combi(new ArrayList<>(), 0, 10, i);
        }
        if (N > 0) System.out.println("-1");
    }
}