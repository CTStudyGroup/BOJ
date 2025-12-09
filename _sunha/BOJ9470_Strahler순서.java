/** BOJ9470_Strahler순서
 * # 문제
 * - 노드 순서 계산 법
 *  - 근원노드(진입차수=0) = 0
 *  - 이외 노드 = 가장 큰 진입차수 i가 1개 = i || 가장 큰 진입차수 i가 2개 이상 = i+1
 * - 노드 M = 바다와 만나는 노드
 * - 목적: Strahler 순서(노드 M의 순서)를 구하는 프로그램
 * - 출력 형식: (테스트 케이스 번호) (strahler 순서)
 *
 * # 제한
 * - 1초
 * - 128초
 * - 1 ≤ T ≤ 1000
 * - 2 ≤ M(노드 수) ≤ 1000
 *
 * # 풀이
 * - 자료구조: 진입을 기준으로 하는 인접행렬/순서 배열
 * - 진입차수가 0이면 순서가 1
 * - 진입차수가 1이상이면 모든 부모를 다 탐색해서 비교 후 값 채워 넣기..
 *
 * - 아무리 봐도 재귀로 M부터 거꾸로 올라가야할 것 같음...
 *
 */

import java.io.*;
import java.util.*;

public class BOJ9470_Strahler순서 {
    static int T,K,M,P;
    static List<Integer>[] gp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        for (int t=0; t<T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            K = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            P = Integer.parseInt(st.nextToken());

            gp = new ArrayList[M];
            for (int m = 0; m < M; m++) {
                gp[m] = new ArrayList<>();
            }

            for (int p = 0; p < P; p++) {
                st = new StringTokenizer(br.readLine());
                int n1 = Integer.parseInt(st.nextToken()) - 1;
                int n2 = Integer.parseInt(st.nextToken()) - 1;
                gp[n2].add(n1);
            }

            System.out.println(K + " " + strahler(M - 1));
        }
    }

    static int strahler(int node){
        // 만약 gp[node]의 리스트 길리가 0이면 근접노드 이므로 1을 return
        if (gp[node].isEmpty()) return 1;

        // 그렇지 않을 경우
        // 리스트를 돌면서 상위 노드의 Strahler 순서를 받아와서 저장 및, 최댓값 구하기

        int i, max = 0;
        int[] cnt = new int[M];
        for (int next: gp[node]) {
            i = strahler(next);
            cnt[i]++;
            max = Math.max(max, i);
        }

        // 최댓값에 해당하는 수가 2개 이상이면 i+1 한개면 i를 return
        if (cnt[max] == 1) return max;
        else return max + 1;
    }
}
