import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        List<Integer>[] graph = new ArrayList[N + 1];
        int[] indegree = new int[N + 1];
        int[] time = new int[N + 1];      // 각 건물 자체 시간
        int[] result = new int[N + 1];    // 누적 결과 시간

        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());

            time[i] = Integer.parseInt(st.nextToken());

            while (true) {
                int pre = Integer.parseInt(st.nextToken());
                if (pre == -1) break;

                // pre → i (선행 건물 → 현재 건물)
                graph[pre].add(i);
                indegree[i]++;
            }
        }

        Queue<Integer> q = new LinkedList<>();

        // 진입차수 0 → 바로 지을 수 있는 건물
        for (int i = 1; i <= N; i++) {
            if (indegree[i] == 0) {
                q.add(i);
                result[i] = time[i];
            }
        }

        while (!q.isEmpty()) {
            int now = q.poll();

            for (int next : graph[now]) {

                // 누적 시간 업데이트 (선행 중 가장 오래 걸린 케이스 선택)
                result[next] = Math.max(result[next], result[now] + time[next]);

                indegree[next]--;
                if (indegree[next] == 0) {
                    q.add(next);
                }
            }
        }

        // 출력
        for (int i = 1; i <= N; i++) {
            System.out.println(result[i]);
        }
    }
}
