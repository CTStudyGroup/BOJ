import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class 이분_그래프_1707 {

    static ArrayList<Integer>[] adj;
    static Node[] nodes;
    static boolean flag;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());

        for (int i = 0; i < K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());

            adj = new ArrayList[V + 1];
            nodes = new Node[V + 1];
            for (int vertexId = 1; vertexId <= V; vertexId++) {
                adj[vertexId] = new ArrayList<>();
                nodes[vertexId] = new Node(vertexId);
            }

            for (int j = 0; j < E; j++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                adj[u].add(v);
                adj[v].add(u);
            }

            flag = true;

            for (int j = 1; j <= V; j++) {
                if (!flag) {
                    break;
                }
                if (nodes[j].color == 0) {
                    bfs(j);
                }
            }
            System.out.println(flag ? "YES" : "NO");
        }
    }

    private static void bfs(int i) {
        Deque<Integer> q = new LinkedList<>();
        q.add(i);
        nodes[i].color = 1;
        while (!q.isEmpty()) {
            Integer vertexId = q.pollFirst();
            Node currentNode = nodes[vertexId];

            for (int adjV : adj[vertexId]) {
                Node nextNode = nodes[adjV];

                if (nextNode.color == 0) {
                    nextNode.color = -currentNode.color;
                    q.add(nextNode.id);
                } else if (nextNode.color == currentNode.color) {
                    flag = false;
                    return;
                }
            }
        }
    }

    static class Node {
        int id;
        int color = 0;

        public Node(int id) {
            this.id = id;
        }
    }
}
