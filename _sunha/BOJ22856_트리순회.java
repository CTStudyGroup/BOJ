/** BOJBOJ22856_트리순회
 * # 문제
 * -
 *
 * # 제한
 *
 *
 * # 풀이
 *
 *
 */

import java.io.*;

public class BOJ22856_트리순회 {

    static class Node {
        int left, right;

        void set(int left, int right) {
            this.left = left;
            this.right = right;
        }
    }

    static int N, cnt, endNode;
    static Node[] tree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        String[] temp;
        tree = new Node[N+1];
        int now;
        for (int n=0; n<N; n++){
            temp = br.readLine().split(" ");
            now = Integer.parseInt(temp[0]);

            tree[now] = new Node();
            tree[now].set(Integer.parseInt(temp[1]), Integer.parseInt(temp[2]));
        }

        endNode = 1;
        while (tree[endNode].right != -1) {
            endNode = tree[endNode].right;
        }

        travel(1);
    }

    static void travel(int now) {
        cnt++;

        if (tree[now].left > 0) {
            travel(tree[now].left);
            cnt++;
        }

        if (tree[now].right > 0) {
            travel(tree[now].right);
            cnt++;
        }

        if (now == endNode) {
            System.out.println(cnt - 1); // 시작점 카운트(1) 제외하고 출력
        }

    }
}
