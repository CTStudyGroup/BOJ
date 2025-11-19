import java.util.*;
import java.io.*;

public class Main {

    static int N, M;
    static char[][] board;

    // 4방향
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static class State {
        int rx, ry;  // Red position
        int bx, by;  // Blue position
        int depth;   // tilt count

        State(int rx, int ry, int bx, int by, int depth) {
            this.rx = rx;
            this.ry = ry;
            this.bx = bx;
            this.by = by;
            this.depth = depth;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new char[N][M];

        int rx = 0, ry = 0, bx = 0, by = 0;

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                board[i][j] = line.charAt(j);

                if (board[i][j] == 'R') {
                    rx = i;
                    ry = j;
                } else if (board[i][j] == 'B') {
                    bx = i;
                    by = j;
                }
            }
        }

        System.out.println(bfs(rx, ry, bx, by));
    }

    static int bfs(int rx, int ry, int bx, int by) {

        boolean[][][][] visited = new boolean[N][M][N][M];
        Queue<State> q = new LinkedList<>();
        q.add(new State(rx, ry, bx, by, 0));
        visited[rx][ry][bx][by] = true;

        while (!q.isEmpty()) {
            State cur = q.poll();

            if (cur.depth >= 10) return -1;

            for (int dir = 0; dir < 4; dir++) {

                // 공 굴리기
                int[] rNext = move(cur.rx, cur.ry, dir);
                int[] bNext = move(cur.bx, cur.by, dir);

                int nrx = rNext[0], nry = rNext[1];
                int nbx = bNext[0], nby = bNext[1];
                int rCount = rNext[2];
                int bCount = bNext[2];

                // 파란 구슬 빠짐 → 실패
                if (board[nbx][nby] == 'O') continue;

                // 빨간 구슬만 빠짐 → 성공
                if (board[nrx][nry] == 'O') return cur.depth + 1;

                // 위치가 겹치면 더 많이 이동한 공을 한 칸 뒤로
                if (nrx == nbx && nry == nby) {
                    if (rCount > bCount) {
                        nrx -= dx[dir];
                        nry -= dy[dir];
                    } else {
                        nbx -= dx[dir];
                        nby -= dy[dir];
                    }
                }

                if (!visited[nrx][nry][nbx][nby]) {
                    visited[nrx][nry][nbx][nby] = true;
                    q.add(new State(nrx, nry, nbx, nby, cur.depth + 1));
                }
            }
        }

        return -1;
    }

    // 공 굴리기 함수: {끝난 x, 끝난 y, 이동 칸 수}
    static int[] move(int x, int y, int dir) {
        int count = 0;

        while (true) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (board[nx][ny] == '#') break;

            x = nx;
            y = ny;
            count++;

            if (board[x][y] == 'O') break;
        }

        return new int[]{x, y, count};
    }
}
