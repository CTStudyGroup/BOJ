import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int[] in, post, pos;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        in = new int[N];
        post = new int[N];
        pos = new int[N + 1];

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            in[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            post[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N; i++) {
            pos[in[i]] = i;
        }

        solve(0, N - 1, 0, N - 1);
        System.out.println(sb);
    }

    static void solve(int inStart, int inEnd, int postStart, int postEnd) {
        if (inStart > inEnd || postStart > postEnd) return;

        int root = post[postEnd];
        sb.append(root).append(' ');

        int rootIndex = pos[root];
        int leftSize = rootIndex - inStart;

        solve(inStart, rootIndex - 1, postStart, postStart + leftSize - 1);
        solve(rootIndex + 1, inEnd, postStart + leftSize, postEnd - 1);
    }
}
