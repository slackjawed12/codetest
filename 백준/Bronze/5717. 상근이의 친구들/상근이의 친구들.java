import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solve(List<List<Integer>> friends) {
        return friends.stream().mapToInt(x->x.stream().reduce(0, Integer::sum)).toArray();
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    List<List<Integer>> friends = new ArrayList<>();
    int[] answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(friends);
        output();
    }

    public void input() throws Exception {
        String[] str = rd.readLine().split(" ");
        while (!(str[0].equals("0") && str[1].equals("0"))) {
            friends.add(List.of(Integer.parseInt(str[0]), Integer.parseInt(str[1])));
            str = rd.readLine().split(" ");
        }
    }


    public void output() throws Exception {
        for (int i : answer) {
            wr.write(i + "\n");
        }
        wr.flush();
        wr.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}
