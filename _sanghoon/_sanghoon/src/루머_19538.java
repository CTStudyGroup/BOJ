import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 루머_19538 {

    static Deque<Integer> q = new LinkedList<>();
    static List<Integer>[] graph;
    static int[] beliefTime;
    static int[] neighborCount;
    static int[] beliefNeighborCount;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            while (true) {
                int neighbor = Integer.parseInt(st.nextToken());
                if (neighbor == 0) break;
                graph[i].add(neighbor);
                graph[neighbor].add(i);
            }
        }

        neighborCount = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            neighborCount[i] = graph[i].size();
        }

        beliefTime = new int[N + 1];
        Arrays.fill(beliefTime, -1);

        beliefNeighborCount = new int[N + 1];

        int M = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int maker = Integer.parseInt(st.nextToken());
            beliefTime[maker] = 0;
            q.offer(maker);
        }

        bfs();

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            sb.append(beliefTime[i]).append(" ");
        }
        System.out.println(sb);
    }

    static void bfs() {
        while (!q.isEmpty()) {
            Integer currentMaker = q.pollFirst();
            for (int nextMaker : graph[currentMaker]) {
                if (beliefTime[nextMaker] == -1) {
                    beliefNeighborCount[nextMaker]++;

                    if (beliefNeighborCount[nextMaker] * 2 >= neighborCount[nextMaker]) {
                        beliefTime[nextMaker] = beliefTime[currentMaker] + 1;
                        q.offer(nextMaker);
                    }
                }
            }
        }

    }

}
