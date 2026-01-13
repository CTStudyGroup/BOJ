/** BOJ1695_팰린드롬 만들기
 * # 문제
 * - 이 수열에 최소 개수의 수를 끼워 넣어 팰린드롬을 만들
 * - 최소 몇 개의 수를 끼워 넣으
 *
 * # 제한
 * - 시간: 2초
 * - 공간: 128MB
 * - 입력
 *  - 1≤N(수열 길이)≤5,000
 *  - 각 수들은 int 범위
 *
 * # 풀이
 * - 같은 수의 개수를 찾아야하는데,,,
 *  - 2332 -> 이렇게 감싸진 형태로 같은 수를 찾아야하거든?
 *  - 꼬인건 둘 중에 아무거나 해도 똑같고
 *  - 동일한 수가 3개 이상일 때는 또 어떻게 처리하지?
 *
 * - 일단 수열의 길이가 5000인거 보면,,,
 *
 * - 그냥 제일 바깥에서 부터 그리디하게?
 *
 * - 아 LCS처럼 최장 공동 부분 수열을 찾는 거네..!
 *
 */

import java.io.*;
import java.util.*;

public class BOJ1695_팰린드롬만들기 {
    public static void main(String[] args) throws IOException {
        // 입력을 빠르게 받기 위해 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // dp[i][j]: 원래 수열의 i번째까지와 뒤집은 수열의 j번째까지의 LCS 길이
        // 메모리 제한(128MB)이 빡빡하므로 int[][] 사용 시 주의 필요하지만, 5000*5000 int는 약 100MB로 통과 가능
        int[][] dp = new int[N + 1][N + 1];

        for(int i = 1; i <= N; i++) {
            for(int j = 1; j <= N; j++) {
                // arr[i]와 뒤집은 수열의 j번째 문자를 비교
                // 뒤집은 수열의 j번째 문자는 원래 수열의 (N - j + 1)번째 문자와 같음
                if(arr[i] == arr[N - j + 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        // 전체 길이 - 가장 긴 팰린드롬 부분 수열의 길이(LCS)
        System.out.println(N - dp[N][N]);
    }
}
