/** BOJ1103_게임
 * # 문제
 * - 1-9 숫자와 구멍이 있는 보드에서 동전을 옴기는게임
 * - 정한 방향으로 동전아래 적힌 숫자만큼 이동
 * - 보드 밖으로 나가거나 구멍에 도착하면 게임종료
 * - 무한히 움직일 수 있다면 -1
 *
 * # 제한
 * - 2초
 * - 512MB
 * - 1 <= N,M 1<= 50
 *
 * # 풀이
 * - 최대 50*50인데 한번에 4가지 경우의 수
 * - 심지어 시작 위치도 안 정해져있는데,,, 완전탐색 절대 안될 것 같은데,,,,
 * - 사실 무한 판정은 거쳐간 자리 다시 도착할 수 있으면 거쳐간 자리기는해.
 *
 * - 아 어떻게 보면 비연결 그래프의 각 부분 연결 그래프 중 가장 노드 수가 많거나 사이클이 있는 경우를 파악하면 되는거잖아?
 * - 그러니까 visited한 영역을 두번 갈 필요가 없음
 * - 최단거리를 구하는 건 아니고 모든 가능 한 수를 구하는 거니까... 다뒤져가 맞겠다..
 * - 아 근데 단순 노드 개수를 구하면 안되고,,, 최장 경로를 구하면될듯? 끝에 도달했을 때, 깊이가 어떻게 되는지를 체크.
 *
 */
import java.io.*;

public class BOJ1103_게임 {

    static int N, M, result=0;
    static int[][] board, visited, dp, ofs = {{-1,0}, {1,0}, {0,-1}, {0,1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);
        board = new int[N][M];
        visited = new int[N][M];
        dp = new int[N][M];


        String row;
        for (int n = 0; n < N; n++) {
            row = br.readLine();
            for (int m = 0; m < M; m++) {
                board[n][m] = row.charAt(m) - '0';
            }
        }

        // for -> visit 하지 않은 노드라면 탐색 시작
        visited[0][0] = 1;
        System.out.println(dfs(0, 0, 1));
    }

    static int dfs(int n, int m, int dpt) {
        dp[n][m] = 1;

        for (int[] o: ofs){
            int nn = n + o[0]*board[n][m];
            int nm = m + o[1]*board[n][m];

            if (check(nn, nm)) {
                // 무한 번이 가능한 경우(사이클 o)
                // -> 같은 경로에서만 체크하기 위해서 아해 visited를 0으로 풀어줘야함.
                // 칸별로 이동 거리가 달라서 0,0에서 왔다고 0,0으로 돌아갈 수 있는 것이 아님.
                if (visited[nn][nm] == 1) {
                    return -1;
                }
                // 사이클 x
                if (visited[nn][nm] == 0) {
                    // 저장된 값 없음
                    if (dp[nn][nm] == 0) {
                        visited[nn][nm] = 1;
                        int result = dfs(nn, nm, dpt + 1);

                        if (result == -1) return -1;
                        dp[n][m] = Math.max(dp[n][m], result + 1);  // nn,nm에서 출발한 모든 경우를 탐색하기 때문에, 최대 값이 보장됨.

                        visited[nn][nm] = 0;
                    }
                    // 저장된 값 있음
                    else dp[n][m] = Math.max(dp[n][m], dp[nn][nm]+1);
                }
            }
        }

        return dp[n][m];
    }

    static boolean check(int n, int m) {
        if (n<0) return false;
        if (m<0) return false;
        if (n>=N) return false;
        if (m>=M) return false;

        return board[n][m] != 24;
    }

}
