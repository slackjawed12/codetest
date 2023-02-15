import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static int IOI(char[] arr, int N) {
        int ans = 0;
        List<Integer> ioi = new ArrayList<>();
        for (int i = 0, j = 0; i < arr.length; i = j) {
            if (arr[i] == 'I') {
                int conti = 0;
                char ex = arr[i];
                while (++j < arr.length && arr[j] != ex) {
                    if (arr[j] == 'I') conti++;
                    ex = arr[j];
                }
                ioi.add(conti);
            } else {
                j++;
            }
        }
        ans = ioi.stream().map(x->x-N+1).filter(x->x>0)
                .reduce(0, Integer::sum);
        return ans;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(rd.readLine());
        int M = Integer.parseInt(rd.readLine());
        char[] arr = rd.readLine().toCharArray();

        System.out.println(IOI(arr, N));
    }
}
