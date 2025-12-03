/** BOJ15684_사다리조작
 * # 문제
 * - N: 세로선 개수 / M: 가로선 개수 / H: 가능한 가로선 위치
 * - 조건: 두 가로선이 연속하거나 접하면 안됨.
 * - 목적: 가로 선을 추가해 사다리 게임 결과 조작 -> i번 세로선 = 결과 i
 * - 출력: 추가해야하는 가로선의 개수
 *
 * # 제산
 * - 변수 범위 -> int 가능
 *  - 2 ≤ N(세로) ≤ 10
 *  - 1 ≤ H(가로) ≤ 30
 *  - 0 ≤ M(가로 후보) ≤ 270(최대)
 *
 *  - 1 ≤ a(연결할 가로 위치) ≤ H
 *  - 1 ≤ b(연결 시작학 세로 위치) ≤ N-1
 *
 * - 시간: 2초 -> 2억번 연산 -> 완전탐색도 가능할지도?
 * - 공간: 512MB -> 넉넉
 *
 * # 풀이
 * - 그래프처럼 생각한다고 치면. 인접 리스트로 해도 될 것같고.
 * - 조작을 어떻게 하냐가 문제인데.
 *  - 개수로 따지면 좀 될 것같거든? 무조건 동일한 b~b+1에서 가로선이 짝수만큼 있어야해. -> 위치는? 뭐 그래프를 다 그려봐?
 *  - 짝수로 만들 때, 어디에 추가해야할지, 위치 탐색만 잘해보자.
 *  - 위치 탐색을 어떻게 해야할까. -> 이걸 완전탐색으로
 *
 * - 짝수인데도 안되는 경우가 있음
 */

//import java.io.*;
//import java.util.*;
//
//public class Main {
//    static boolean result = false;
//    static int N,M,H;
//    static int[][] gp;
//    static int[] cnt;
//    public static void main(String[] args) throws IOException {
//        // 기본 입력 받기
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int N,M,H;
//        String[] temp = br.readLine().split(" ");
//        N = Integer.parseInt(temp[0]);
//        M = Integer.parseInt(temp[1]);
//        H = Integer.parseInt(temp[2]);
//
//        // 인접 행렬 -> gp[b] = a -> b와 b+1이 a에서 연결되어 있다.
//        gp = new int[N+1][M+1];
//        cnt = new int[N+1];
//
//        // M만큼 돌면서 인접 리스트 채우기
//        int a,b;
//
//        for (int m=0; m<M; m++) {
//            temp = br.readLine().split(" ");
//            a = Integer.parseInt(temp[0]);
//            b = Integer.parseInt(temp[1]);
//
//            gp[b][a] = 1;
//            cnt[b] += 1;
////            System.out.println(b + " " + a + " " + cnt[b]);
//        }
//
//
//        // 홀수인 리스트가 3개 이상인 경우 -1 출력
//        int odd_cnt = 0;
//        for (int c: cnt) {
////            System.out.println(c);
//            if (c % 2 == 1) {
//                odd_cnt++;
//            }
//        }
//        if (odd_cnt > 3) {
//            System.out.println(-1);
//            return;
//        }
//
//        // 홀수인 리스트가 2개 이하인 경우
//        dfs(1);
//
//        if (result)
//            System.out.println(odd_cnt);
//        else
//            System.out.println(-1);
//
//    }
//
//    static void dfs(int n) {
//        // n == N이면 true로 바꿈 반환
//        if (n >= N) {
//            result = true;
//            return;
//        }
//
//        // 해당 줄의 가로선이 홀수 개가 아니면 다음줄로 넘어감
//        if (cnt[n] % 2 == 0) {
//            dfs(n+1);
//        }
//
//        // 홀수 개면, 1부터 H까지 돌면서 가능한지 체크
//        for (int h=0; h<H; h++) {
//            // n, n-1, n+1에 해당 가로줄이 없으면 가능함
//            if (gp[n][h] == 0 && gp[n-1][h] == 0 && gp[n+1][h] == 0){
//                gp[n][h] = 1;
//                dfs(n+1);
//                gp[n][h] = 0;
//            }
//        }
//    }
// }
import java.io.*;

public class BOJ15684_사다리조작 {
    static int N,M,H;
    static int[][] gp;
    public static void main(String[] args) throws IOException {
        // 기본 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);
        H = Integer.parseInt(temp[2]);

        // 인접 행렬 -> gp[b] = a -> b와 b+1이 a에서 연결되어 있다.
        gp = new int[N+1][H+1];

        // M만큼 돌면서 채우기
        int a,b;
        for (int m=0; m<M; m++) {
            temp = br.readLine().split(" ");
            a = Integer.parseInt(temp[0]);
            b = Integer.parseInt(temp[1]);

            gp[b][a] = 1;
        }


        for (int r=0; r<4; r++) {
            if (dfs(r)) {
                System.out.println(r);
                return;
            }
        }

        System.out.println(-1);
    }

    static boolean dfs(int remain) {
        if (remain == 0) {
            if (check()) {
                return true;
            }
            return false;
        }

        boolean result = false;

        for (int n=1; n<N; n++) {
            // 1부터 H까지 돌면서 가능한지 체크
            for (int h = 1; h <= H; h++) {
                // n, n-1, n+1에 해당 가로줄이 없으면 가능함
                if (gp[n][h] == 0 && gp[n - 1][h] == 0 && gp[n + 1][h] == 0) {
                    gp[n][h] = 1;
                    result = dfs(remain - 1) || result;
                    gp[n][h] = 0;
                }
            }
        }

        return result;
    }

    static boolean check() {
        for (int n=1; n<=N; n++) {
            int pos = n;
            for (int h = 1; h <= H; h++){
                if (gp[pos][h] == 1) {
                    pos++;
                }
                else if (gp[pos -1][h] == 1) {
                    pos--;
                }
            }
            if (pos != n) return false;
        }
        return true;
    }
}

