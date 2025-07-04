import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;

public class 녹색_옷_입은_애가_젤다지_4485 {
    static int[][] map;
    static int[][] dist;
    static int N;
    static int[][] d = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    static class Node implements Comparable<Node> {
        int r;
        int c;
        int cost;

        public Node(int r, int c, int cost) {
            this.r = r;
            this.c = c;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int problemNum =  0;
        while (true) {
            problemNum ++;
            N = Integer.parseInt(br.readLine());
            if (N == 0) {
                System.out.println(sb);
                return;
            }

            map = new int[N][N];
            dist = new int[N][N];
            for (int i = 0; i < N; i++) {
                map[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                Arrays.fill(dist[i], Integer.MAX_VALUE);
            }

            dijkstra();
            sb.append("Problem ").append(problemNum).append(": ").append(dist[N - 1][N - 1]).append("\n");
        }
    }

    static void dijkstra() {
        PriorityQueue<Node> pq = new PriorityQueue<>();

        dist[0][0] = map[0][0];
        pq.offer(new Node(0, 0, dist[0][0]));

        while (!pq.isEmpty()) {
            Node currentNode = pq.poll();

            if (currentNode.cost > dist[currentNode.r][currentNode.c]) {
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int nr = currentNode.r + d[i][0];
                int nc = currentNode.c + d[i][1];

                if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                    int newCost = currentNode.cost + map[nr][nc];
                    if (newCost < dist[nr][nc]) {
                        dist[nr][nc] = newCost;
                        pq.offer(new Node(nr, nc, newCost));
                    }
                }
            }
        }
    }
}
