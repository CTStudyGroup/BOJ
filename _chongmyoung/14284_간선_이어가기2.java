import java.io.*;
import java.util.*;

class Edge {
    int to, weight;
    Edge(int to, int weight) {
        this.to = to;
        this.weight = weight;
    }
}

public class Main {
    static List<List<Edge>> graph = new ArrayList<>();
    static int[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); // 정점 개수
        int m = Integer.parseInt(st.nextToken()); // 간선 개수

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph.get(u).add(new Edge(v, w));
            graph.get(v).add(new Edge(u, w)); // 무방향 그래프
        }

        st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken()); // 시작점
        int t = Integer.parseInt(st.nextToken()); // 도착점

        dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);

        dijkstra(s);

        System.out.println(dist[t]);
    }

    static void dijkstra(int start) {
        PriorityQueue<Edge> pq = new PriorityQueue<>(Comparator.comparingInt(e -> e.weight));
        dist[start] = 0;
        pq.offer(new Edge(start, 0));

        while (!pq.isEmpty()) {
            Edge cur = pq.poll();
            int node = cur.to;
            int weight = cur.weight;

            if (weight > dist[node]) continue;

            for (Edge next : graph.get(node)) {
                if (dist[next.to] > dist[node] + next.weight) {
                    dist[next.to] = dist[node] + next.weight;
                    pq.offer(new Edge(next.to, dist[next.to]));
                }
            }
        }
    }
}
