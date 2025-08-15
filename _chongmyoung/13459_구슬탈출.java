      import java.io.*;
      import java.util.*;

      public class Main {
          static int N, M;
          static char[][] board;
          static boolean[][][][] visited;
          static int[] dx = {-1, 1, 0, 0}; // 좌, 우, 하, 상
          static int[] dy = {0, 0, -1, 1};

          static class State {
              int rx, ry, bx, by, cnt;
              State(int rx, int ry, int bx, int by, int cnt) { // r = 빨강 위치 / b = 파랑 위치 / cnt = 기울인 횟수
                  this.rx = rx; this.ry = ry; this.bx = bx; this.by = by; this.cnt = cnt;
              }
          }

          public static void main(String[] args) throws IOException {
              BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 빠른 입력
              StringTokenizer st = new StringTokenizer(br.readLine()); // 첫 줄: N, M
              N = Integer.parseInt(st.nextToken());
              M = Integer.parseInt(st.nextToken());
              board = new char[N][M];

              int rx = 0, ry = 0, bx = 0, by = 0;
              for (int i = 0; i < N; i++) { // N줄에  
                  String line = br.readLine(); // i번째 문자열
                  for (int j = 0; j < M; j++) {
                      char c = line.charAt(j);
                      if (c == 'R') { rx = i; ry = j; board[i][j] = '.'; } // 구슬은 움직이기 때문에 빈칸('.')으로 표시해놔야 한다.
                      else if (c == 'B') { bx = i; by = j; board[i][j] = '.'; }
                      else board[i][j] = c; // 구슬이 아니면 입력 받은대로 선언.(#, ., O)
                  }
              }

              visited = new boolean[N][M][N][M]; // 초기좌표 방문 표시
              System.out.println(bfs(rx, ry, bx, by));
          }

          static int bfs(int rx, int ry, int bx, int by) {
              Queue<State> q = new LinkedList<>();
              q.add(new State(rx, ry, bx, by, 0)); // 시작 상태 삽입(기울임 0회)
              visited[rx][ry][bx][by] = true; 

              while (!q.isEmpty()) {
                  State cur = q.poll();
                  if (cur.cnt >= 10) continue;

                  for (int dir = 0; dir < 4; dir++) {
                      int[] rMove = roll(cur.rx, cur.ry, dir); // 빨간구슬 굴리기 결과
                      int[] bMove = roll(cur.bx, cur.by, dir); // 파란구슬  ''

                      // bMove[2] == 1이면 파란 구슬이 구멍에 빠졌다는 뜻 -> 실패 상태, 스킵
                      if (bMove[2] == 1) continue;

                      // rMove[2] == 1이고, 파랑은 안 빠졌으면 설공 -> 1 반환
                      if (rMove[2] == 1) return 1;

                      // 둘 다 같은 위치면 더 많이 이동한 구슬을 한 칸 뒤로
                      if (rMove[0] == bMove[0] && rMove[1] == bMove[1]) {
                          if (rMove[3] > bMove[3]) { // dist(이동 거리)가 더 많다면 
                              rMove[0] -= dx[dir]; // 굴러온 방향으로 한칸 감
                              rMove[1] -= dy[dir];
                          } else {
                              bMove[0] -= dx[dir]; // 굴러온 방향으로 한칸 감
                              bMove[1] -= dy[dir];
                          }
                      }

                      if (!visited[rMove[0]][rMove[1]][bMove[0]][bMove[1]]) {
                          visited[rMove[0]][rMove[1]][bMove[0]][bMove[1]] = true;
                          q.add(new State(rMove[0], rMove[1], bMove[0], bMove[1], cur.cnt + 1));
                      }
                  }
              }
              return 0; // 10회 이내에 성공 못 하면 0
          }

          // 현재(x, y)에서 dir 방향으로 벽('#')을 만나기 전까지 굴림
          // 구멍을 만나면 즉시 종료.
          // 반환값: 멈춘x, 멈춘y, 구멍여부(1이면 빠짐, 0이면 안빠짐), 이동거리
          static int[] roll(int x, int y, int dir) {
              int dist = 0; // 이동거리 카운트
              while (board[x + dx[dir]][y + dy[dir]] != '#') { // 다음 칸이 벽이 아니면 계속 전진
                  x += dx[dir];
                  y += dy[dir];
                  dist++;
                  if (board[x][y] == 'O') // 구멍 만났을때
                    return new int[]{x, y, 1, dist}; // 현재좌표, 구멍여부=1, 이동거리 반환
              }
              // 벽 바로 앞에서 멈춘 경우(벽에 막힌 경우): 구멍에 빠지지 않음(0)
              return new int[]{x, y, 0, dist};
          }
      }
