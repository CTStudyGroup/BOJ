import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] cost;
    static int[] dp; // 메모이제이션 배열

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        cost = new int[N][N];
        // 비트마스크 범위: 0 ~ (2^N - 1)
        dp = new int[1 << N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                cost[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // DP 배열 초기화 (0은 아직 방문하지 않음을 의미)
        // 비용이 0일 수도 있는 문제라면 -1로 초기화하는 것이 안전하지만,
        // 여기서는 최소값을 구하고 합이 0보다 크므로 0체크로도 가능.
        // 하지만 정석대로 0 처리를 위해 main에서는 호출만 함.
        
        System.out.println(dfs(0, 0));
    }

    // person: 현재 작업을 배정할 사람의 번호 (0 ~ N-1)
    // mask: 현재까지 배정된 일(Task)의 목록을 나타내는 비트마스크
    static int dfs(int person, int mask) {
        // 기저 조건: 모든 사람에게 일을 배정했으면 비용 0 반환
        if (person == N) {
            return 0;
        }

        // 이미 계산된 상태라면 저장된 값 반환 (메모이제이션)
        if (dp[mask] != 0) {
            return dp[mask];
        }

        int minCost = Integer.MAX_VALUE;

        // 현재 사람(person)에게 어떤 일(i)을 맡길지 탐색
        for (int i = 0; i < N; i++) {
            // i번째 일이 아직 배정되지 않았다면 (mask의 i번째 비트가 0이라면)
            if ((mask & (1 << i)) == 0) {
                // 재귀 호출: 다음 사람, 마스크 업데이트, 비용 합산
                minCost = Math.min(minCost, dfs(person + 1, mask | (1 << i)) + cost[person][i]);
            }
        }

        // 계산된 최소 비용을 저장하고 반환
        return dp[mask] = minCost;
    }
}
