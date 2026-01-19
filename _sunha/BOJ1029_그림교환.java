/** BOJ1029_그림교환
 * # 문제
 * 그림 거래를 하는데,
 * 1. 동일한 가격 or 더 큰 가격으로만 팔 수 있음
 * 2. 한 사람당 한번씩 살 수 잇음
 *
 * 그림 소유자의 최대 수를 출력
 *
 * 주어지는 값은 그래프다... (i,j) -> j번 예술가가 i번 예술가에게 그림을 살때의 가격
 *
 * # 제한
 * - 2초
 * - 128MB
 * - 2 <= N <= 15
 * - 0 <= 가격 <= 9
 *
 * # 풀이
 * - 어려운 그래프탐색을 써야하나했는데
 * - 그냥 모든 경로를 탐색하는 완전탐색으로 가능하지 않을까...? 하는 생각이 들긴하는데
 * - 각 순서에서의 선택지를 다 곱한 것 최대 14! = 100억이 넘네 10!이 3백만 정도임.
 * - 안됨...
 *
 * - 그럼 어려운 그래프 탐색을 써야하는 거 같음
 * - 근데 이거 모름.
 * - 아마 다익스트라, 플로이드와샬, 벨만포드 -> 근데 이거 다 최단 경로를 구하는 알고리즘인데...?
 *
 * - DFS + DP로?
 * - 팔린 가격을 기준으로 해보자.
 * - 외판원 순회처럼? 어디를 마지막으로 방문했는지가 중요하잖아.
 * - [비트마스킹으로 방문한곳, 현재 가격]을 하면 될 것같아.
 *
 */

import java.io.*;

public class BOJ1029_그림교환 {
    static int N, maxCnt=0;
    static String[] cost;
    static int[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력받기
        N = Integer.parseInt(br.readLine());
        cost = new String[N];
        for (int n = 0; n<N ; n++) {
            cost[n] = br.readLine();
        }

        // DP만들기. N개의 bit로 표현하는 수가... 2^16 - 1 = 니까 int안에 표현 가능.
        // 근데 128MB면 ... 4MB = 100만개 -> 3200만개까지
        // 2^16 * 10 면 충분히 가능하네..

        // DP 배열을 [2^N-1, N] 크기로 만들면됨. -> 무조건 1에서 시작이니까.
        // 그러면 초기 위치는 [0,0]이 되겠지. (예술가는 0부터 N-1로 만들기)
        dp = new int[1 << (N+1)][N];
        // 초기화
        for (int r = 0; r < 1 << (N+1); r++) {
            for (int c = 0; c < N; c++) {
                dp[r][c] = Integer.MAX_VALUE;
            }
        }

        // DP[경로][현재 위치]
        // = 그림을 구매할 수 있는 최소 가격.
        // = min(for -> (DP[현재 위치 뺀 경로][n] + n에서 현재 위치로 파는 가격))


        // 순서는 해당 경로에 대한 모든 n을 구하고, +1된 경로로.

        dp[1][0] = 0; // 이미 1번이 가지고 있음.
        a(1,0);

        System.out.println(maxCnt);
    }

    static void a(int route, int prev) {
        int currentPeopleCount = Integer.bitCount(route);
        maxCnt = Math.max(maxCnt, currentPeopleCount);

        for (int n = 0; n < N; n++) {
            int mask = 1<<n;
            if ((route & mask) != 0)  // 이미 거쳐온 경로
                continue;

            // 갈 수 있는 경로면,
            // 아까 전 위치에서 지금 위치로 파는 가격을 현재 가격이랑 비교해봐야겠지.
            if (dp[route][prev] <= cost[prev].charAt(n) - '0' && dp[route|mask][n] > cost[prev].charAt(n) - '0'){
                dp[route|mask][n] = cost[prev].charAt(n) - '0';
                a(route|mask, n);
            }
        }
    }
}
