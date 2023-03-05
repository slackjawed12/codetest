import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class BST {
    Node root;

    public BST() {

    }

    public BST(Node root) {
        this.root = root;
    }

    void addByPreorder(int x) {
        if (root == null) {
            root = new Node(x);
            return;
        }

        if (root.val > x) {
            if (root.left == null) {
                root.left = new BST(new Node(x));
            } else {
                root.left.addByPreorder(x);
            }
        } else {
            if (root.right == null) {
                root.right = new BST(new Node(x));
            } else {
                root.right.addByPreorder(x);
            }
        }
    }

    void PostTraverse(List<Integer> l) {
        if(root.left!=null) root.left.PostTraverse(l);
        if(root.right!=null) root.right.PostTraverse(l);
        l.add(root.val);
    }

    class Node {
        BST left;
        BST right;
        int val;

        Node(int val) {
            this.val = val;
        }
    }
}

class Solution {
    public List<Integer> solve(int[] preorders) {
        BST bst = new BST();
        for (int i : preorders) {
            bst.addByPreorder(i);
        }
        List<Integer> ans = new ArrayList<>();
        bst.PostTraverse(ans);

        return ans;
    }
}

public class Main {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int[] preorders;
    List<Integer> answer;

    public void submit() throws Exception {
        input();
        answer = new Solution().solve(preorders);
        output();
    }

    public void input() throws Exception {
        List<String> inputs = new ArrayList<>();
        String str;
        while ((str = rd.readLine()) != null) {
            inputs.add(str);
        }
        preorders = new int[inputs.size()];
        for (int i = 0; i < preorders.length; i++) {
            preorders[i] = Integer.parseInt(inputs.get(i));
        }
    }

    public void output() {
        for (int j : answer) {
            System.out.println(j);
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().submit();
    }
}