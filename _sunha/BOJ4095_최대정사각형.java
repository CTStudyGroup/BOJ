import java.io.*;
import java.util.*;

public class BOJ4095_최대정사각형 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            String line = br.readLine();

            st = new StringTokenizer(line);

            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            // 종료 조건
            if (N == 0 && M == 0) break;

            int[][] dp = new int[N][M];
            int maxSide = 0;

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < M; j++) {
                    int val = Integer.parseInt(st.nextToken());

                    if (val == 1) {
                        dp[i][j] = 1; // 기본값 1

                        if (i > 0 && j > 0) {
                            dp[i][j] = Math.min(dp[i-1][j-1], Math.min(dp[i-1][j], dp[i][j-1])) + 1;
                        }

                        // 최댓값 갱신
                        maxSide = Math.max(maxSide, dp[i][j]);
                    }
                }
            }

            System.out.println(maxSide);
        }
    }
}