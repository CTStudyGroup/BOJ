import java.io.*;
import java.util.*;

public class Main {
    static int N, K, L;
    static int[][] board;
    static Map<Integer, Character> moves = new HashMap<>();
    static Deque<int[]> snake = new LinkedList<>();

    // 상, 우, 하, 좌 (시계 방향)
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];

        K = Integer.parseInt(br.readLine());
        for (int i = 0; i < K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            board[x][y] = 1; // 사과
        }

        L = Integer.parseInt(br.readLine());
        for (int i = 0; i < L; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            char c = st.nextToken().charAt(0);
            moves.put(t, c);
        }

        System.out.println(simulate());
    }

    static int simulate() {
        int time = 0;
        int dir = 1; // 처음에 오른쪽
        snake.add(new int[]{0, 0});

        while (true) {
            time++;
            int[] head = snake.peekLast();
            int nx = head[0] + dx[dir];
            int ny = head[1] + dy[dir];

            // 벽 충돌
            if (nx < 0 || ny < 0 || nx >= N || ny >= N) return time;

            // 자기 몸 충돌
            for (int[] part : snake) {
                if (part[0] == nx && part[1] == ny) return time;
            }

            // 이동
            if (board[nx][ny] == 1) { // 사과가 있으면
                board[nx][ny] = 0;
                snake.add(new int[]{nx, ny}); // 머리만 늘림
            } else {
                snake.add(new int[]{nx, ny});
                snake.pollFirst(); // 꼬리 줄임
            }

            // 방향 전환 확인
            if (moves.containsKey(time)) {
                char c = moves.get(time);
                if (c == 'L') dir = (dir + 3) % 4;
                else dir = (dir + 1) % 4;
            }
        }
    }
}
