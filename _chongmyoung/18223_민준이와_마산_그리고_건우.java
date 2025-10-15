import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {
    int vertex;
    int cost;
    Node(int vertex, int cost) {
        this.vertex = vertex;
        this.cost = cost;
    }
    @Override
    public int compareTo(Node o) {
        return this.cost - o.cost;
    }
}

public class Main {
    static final int INF = Integer.MAX_VALUE;
    static List<List<Node>> graph = new ArrayList<>();
    static int[] dist;

    static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        Arrays.fill(dist, INF);
        dist[start] = 0;
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (cur.cost > dist[cur.vertex]) continue;
            for (Node next : graph.get(cur.vertex)) {
                int newCost = dist[cur.vertex] + next.cost;
                if (newCost < dist[next.vertex]) {
                    dist[next.vertex] = newCost;
                    pq.offer(new Node(next.vertex, newCost));
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        for (int i = 0; i <= V; i++)
            graph.add(new ArrayList<>());
        dist = new int[V + 1];

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph.get(u).add(new Node(v, w));
            graph.get(v).add(new Node(u, w));
        }

        dijkstra(1);
        int D1 = dist[V];
        int D1toP = dist[P];

        dijkstra(P);
        int PtoV = dist[V];

        if (D1toP + PtoV <= D1)
            System.out.print("SAVE HIM");
        else
            System.out.print("GOOD BYE");
    }
}
