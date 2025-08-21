import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] meetings = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            meetings[i][0] = Integer.parseInt(st.nextToken()); // 시작 시간
            meetings[i][1] = Integer.parseInt(st.nextToken()); // 종료 시간
        }

        // 시작 시간 기준 정렬
        Arrays.sort(meetings, (a, b) -> a[0] - b[0]);

        // 우선순위 큐 → 종료 시간이 빠른 회의가 먼저 나옴
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int[] meeting : meetings) {
            // 현재 회의 시작이 가장 빨리 끝나는 회의보다 늦거나 같으면 → 같은 방 사용 가능
            if (!pq.isEmpty() && pq.peek() <= meeting[0]) {
                pq.poll();
            }
            // 새 회의 종료 시간 추가
            pq.offer(meeting[1]);
        }

        // 남아 있는 회의실 개수 = 필요한 최소 회의실 개수
        System.out.println(pq.size());
    }
}
