import java.io.*;
import java.util.*;

public class Main {
  static int N;
  static int[][] G; // 각 칸의 꽃 대여 비용
  static boolean[][] visited;
  static int answer = Integer.MAX_VALUE;
  static int[] dx = {0, 0, 1, -1};
  static int[] dy = {1, -1, 0, 0};

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    N = Integer.parseInt(br.readLine());
    G = new int[N][N];

    for (int i = 0; i < N; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int j = 0; j < N; j++) {
            G[i][j] = Integer.parseInt(st.nextToken());
        }
    }

    visited = new boolean[N][N]; // 모든 칸 방문 여부 초기화
    dfs(0, 0); // 꽃 0개 심은 상태에서 DFS 시작
    System.out.println(answer); // 최소 비용 출력
  }

  // DFS 꽃 심기 탐색
  static void dfs(int depth, int cost) {
    // 현재 누적 비용이 이미 최소값보다 크면 더 볼 필요 없음 -> 가지치기
    if(cost >= answer) return;

    // 꽃 3개를 모두 심었으면 최소값 갱신 후 종료
    if(depth == 3){
      answer = Math.min(answer, cost);
      return;
    }

    for(int i = 1; i < N - 1; i++){
      for(int j = 1; j < N - 1; j++){
        if(canPlant(i, j)){
          int addCost = plant(i, j);

          dfs(depth + 1, cost + addCost);

          remove(i, j);
        }
      }
    }
  }

      //중심 및 상하좌우 4칸 모두 비어 있어야 함
      static boolean canPlant(int x, int y) {
          if (visited[x][y]) return false; // 중심이 이미 점유됨
          for (int k = 0; k < 4; k++) {
              int nx = x + dx[k], ny = y + dy[k];
              if (visited[nx][ny]) return false; // 꽃잎 위치 중 하나라도 점유되어 있으면 불가능
          }
          return true;
      }

      //꽃 심기, 꽃이 차지하는 칸들의 비용 합을 반환
      static int plant(int x, int y) {
          int sum = G[x][y]; // 중심 비용
          visited[x][y] = true; // 중심 방문 처리

          // 상하좌우 꽃잎 방문 처리 및 비용 합산
          for (int k = 0; k < 4; k++) {
              int nx = x + dx[k], ny = y + dy[k];
              sum += G[nx][ny];
              visited[nx][ny] = true;
          }
          return sum;
      }

      //심은 꽃의 중심과 꽃잎을 다시 visited=false로 되돌림
      static void remove(int x, int y) {
          visited[x][y] = false; // 중심 해제
          for (int k = 0; k < 4; k++) {
              int nx = x + dx[k], ny = y + dy[k];
              visited[nx][ny] = false; // 꽃잎 해제
          }
      }
  }
