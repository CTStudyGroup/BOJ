import java.io.*;
import java.util.*;

public class BOJ23288_주사위굴리기2 {
    static int[][] gp, visited, count;
    static int[] dice = {6,3,5};    // 바닥면, 오른쪽 면, 아래쪽 면
    static int[][] offset = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    static int dir;                 // 0=동 / 1=남 / 2=서 / 3=북
    static int N, M, K;
    static ArrayList<int[]> edit_count;

    public static void main(String[] args) throws IOException {
        // get input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);
        K = Integer.parseInt(temp[2]);

        // set graph
        gp = new int[N][M];
        visited = new int[N][M];
        count = new int[N][M];

        for (int n=0; n<N; n++) {
            temp = br.readLine().split(" ");
            for (int m=0; m<M; m++) {
                gp[n][m] = Integer.parseInt(temp[m]);
            }
        }

        // for 0 -> K
        int x = 0, y = 0, score = 0;
        for (int k=0; k<K; k++) {
            // move
            x += offset[dir][0];
            y += offset[dir][1];

            // 갈  수 없는 칸일 때
            if (x < 0 || x >= N || y < 0 || y >= M) {
                x -= offset[dir][0];
                y -= offset[dir][1];
                rotateOppo();
                x += offset[dir][0];
                y += offset[dir][1];
            }

            // roll
            roll();

            // 점수 계산(count or dfs+setCount -> 두번에 나눠서 하는 거 좀 비효율 적임...)
            int adjecanct;
            if (count[x][y] != 0) adjecanct = count[x][y];
            else {
                edit_count = new ArrayList<>();
                adjecanct = dfs(x, y);
                setCount(adjecanct);
            }
            score += adjecanct * gp[x][y];

            // rotate
            if (dice[0] > gp[x][y]) rotateCW();
            else if (dice[0] < gp[x][y]) rotateCCW();
        }
        System.out.println(score);
    }

    static int dfs(int x, int y) {
        int val = gp[x][y];
        int result = 1; // 자기 자신 포함
        visited[x][y] = 1;
        edit_count.add(new int[] {x, y});

        // for 0->4 하면서 상하좌우 탐색
        for (int o=0; o<4; o++) {
            int nx = x+offset[o][0];
            int ny = y+offset[o][1];

            // 가능한 경우(경계 안이고, 같은 수를 가졌으며, visit하지 않음)
            if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
                if (visited[nx][ny] == 0 && gp[nx][ny] == val){
                    result += dfs(nx, ny);
                    // visited[nx][ny] = 0; -> 경로 찾는게 아니라 그냥 해도 될 것같은데... 안바꾸고.
                }
            }
        }
        return result;
    }

    static void setCount(int cnt) {
        for (int[] pos: edit_count) {
            count[pos[0]][pos[1]] = cnt;
        }
    }

    static void rotateCW() {
        dir = (dir+1)%4;
    }

    static void rotateCCW() {
        dir = (dir+3)%4;
    }

    static void rotateOppo() {
        dir = (dir+2)%4;
    }

    static void roll( ) {
        int[] new_dice = dice;

        switch (dir) {
            case 0:     // 동
                new_dice = new int[] {dice[1], 7 - dice[0], dice[2]};
                break;
            case 1:     // 남
                new_dice = new int[] {dice[2], dice[1], 7 - dice[0]};
                break;
            case 2:     // 서
                new_dice = new int[] {7 - dice[1], dice[0], dice[2]};
                break;
            case 3:     // 북
                new_dice = new int[] {7 - dice[2], dice[1], dice[0]};
                break;
        }

        dice = new_dice;
    }
}