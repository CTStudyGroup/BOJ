import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] coin; // H=0, T=1

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        coin = new int[N][N];

        for (int i = 0; i < N; i++) {
            String line = br.readLine().replace(" ", "");
            for (int j = 0; j < N; j++) {
                coin[i][j] = (line.charAt(j) == 'T') ? 1 : 0;
            }
        }

        int answer = Integer.MAX_VALUE;

        // 행 뒤집기 여부를 비트마스크로 표현
        for (int mask = 0; mask < (1 << N); mask++) {
            int sum = 0;

            // 열 기준으로 T개 계산
            for (int col = 0; col < N; col++) {
                int tCount = 0;

                for (int row = 0; row < N; row++) {
                    int val = coin[row][col];

                    // mask에서 row번째 비트가 1이면 행 뒤집기 발생
                    if ((mask & (1 << row)) != 0) {
                        val ^= 1; // 0↔1 flip
                    }

                    if (val == 1) tCount++;
                }

                // 이 열에서 뒤집지 않고 T 개수 tCount
                // 이 열을 뒤집으면 H<->T 이므로 T 개수는 N - tCount
                sum += Math.min(tCount, N - tCount);
            }

            answer = Math.min(answer, sum);
        }

        System.out.println(answer);
    }
}
