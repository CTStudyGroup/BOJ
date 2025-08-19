import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 학생 수
        int K = Integer.parseInt(st.nextToken()); // 등수 차이 제한

        // 이름 길이 저장 배열
        int[] lengths = new int[N];
        for (int i = 0; i < N; i++) {
            String name = br.readLine();
            lengths[i] = name.length(); // 이름 길이만 저장
        }

        // 큐 배열 (이름 길이 별 학생 수 카운트)
        Queue<Integer>[] queues = new LinkedList[21]; // 이름 길이 2~20
        for (int i = 0; i <= 20; i++) {
            queues[i] = new LinkedList<>();
        }

        long answer = 0;

        for (int i = 0; i < N; i++) {
            int len = lengths[i];

            // 현재 학생의 이름 길이 큐
            Queue<Integer> q = queues[len];

            // 윈도우 범위 유지 (K 등수 이상 차이나면 제거)
            while (!q.isEmpty() && i - q.peek() > K) {
                q.poll();
            }

            // 같은 이름 길이를 가진 학생 수만큼 "좋은 친구" 추가
            answer += q.size();

            // 현재 학생을 큐에 추가
            q.offer(i);
        }

        System.out.println(answer);
    }
}
