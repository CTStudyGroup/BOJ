import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 막걸리 통 개수
        int K = Integer.parseInt(st.nextToken()); // 사람 수

        int[] arr = new int[N];
        long max = 0; // 탐색 범위의 최댓값

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            max = Math.max(max, arr[i]);
        }

        long left = 1;   // 최소 용량
        long right = max;
        long answer = 0;

        while (left <= right) {
            long mid = (left + right) / 2;

            long cnt = 0; // mid ml씩 나눴을 때 몇 명에게 줄 수 있는지 계산
            for (int vol : arr) {
                cnt += vol / mid;
            }

            if (cnt >= K) {
                // K명 이상 나눠줄 수 있다면 더 크게 줄 수 있는지 탐색
                answer = mid;
                left = mid + 1;
            } else {
                // K명에게 못 나눠준다면 용량을 줄여야 함
                right = mid - 1;
            }
        }

        System.out.println(answer);
    }
}
