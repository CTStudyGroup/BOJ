/** BOJ17779_게리맨더링2
 * # 문제
 * - 5개의 선거구 공평하게 나누기
 * - 구역
 *  - 무조건 선거구 하나에 포함되어야함
 *  -
 *
 * - 구할 것: 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값
 *
 * # 제한
 * - 1초
 * - 512MB
 * - 5 ≤ N ≤ 20
 * - 1 ≤ A[r][c] ≤ 100
 *
 * # 풀이
 * - 아니 주어지는 게 N밖에 없는데...
 * - 완전탐색? 1초 안에 가능할가?
 *
 * - 꼭짓점 4개 찍고?
 * - 4모서리에서 대각선으로 합을 만들어가는 거? 다 구해놔?
 *
 * - 아니야 문제에 기반해서 주어지는 변수가 -> x, y, d1, d2 -> 이걸 그냥 무지성으로 다 둘려볼까? 20ㅣ니까
 * - 심지어 그래프탐핵도 아니니까 완전괜찮을 것 같은데 해봤자 한번에 400개 씩 연산 * (러프하게 경우의 수 계산해서 20^4 = 160000) = 64000000 -> 넉넉함.
 */

import java.io.*;
import java.util.*;

public class BOJ17779_게리맨더링2 {
    public static void main(String[] args) throws IOException {
        int[][] city;
        int[] population;
        int N, diff = Integer.MAX_VALUE;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        city = new int[N+1][N+1];

        for (int i=1; i<=N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=1; j<=N; j++) {
                city[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int x=1; x<=N; x++) {
            for (int y=1; y<=N; y++) {
                for (int d2=1; d2<=N-y; d2++) {
                    for (int d1=1; d1<=y; d1++) {

                        population = new int[5];
                        for (int r=1; r<=N; r++) {
                            for (int c=1; c <=N; c++) {
                                int now = city[r][c];

                                // 각 구역 판별
                                if (r < x+d1 && c <= y && (x+y) > (r+c)) population[0] += now;
                                else if (r <= x+d2 && y < c && (x-y) > (r-c)) population[1] += now;
                                else if (x+d1<=r && c < y-d1+d2 && (x-y+(2*d1) < (r-c))) population[2] += now;
                                else if (x+d2<r && y-d1+d2 <= c && (x+y+(2*d2) < (r+c))) population[3] += now;
                                else population[4] += now;
                            }
                        }
                        int max_p = 0, min_p = Integer.MAX_VALUE;
                        for (int i=0; i<5; i++) {
                            if (population[i] > max_p) max_p = population[i];
                            if (population[i] < min_p) min_p = population[i];
                        }
                        if ((max_p - min_p) < diff) {
                            diff = max_p - min_p;
                        }
                    }
                }
            }
        }
        System.out.println(diff);
    }
}
