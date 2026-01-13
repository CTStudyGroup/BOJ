/** BOJ1030_프렉탈평면
 * # 문제
 * - 0시간: 흰섹 정사각형 1개
 * - 1시간: 각 정사각형 NXN개, 분할 후 흰색으로 둘러쌓인 K×K 정사각형은 검정색
 *
 * # 제한
 * - 2초
 * - 128MB -> 32백만개
 * - 0 ≤ s(시간) ≤ 10
 * - 3 ≤ N(분할 개수) ≤ 8
 * - 1 ≤ K(검정색) ≤ N - 2
 * - (N - K) mod 2 = 0 -> NK는 2배 차이
 * - 0 ≤ R1, R2, C1, C2 (출력 위치) ≤ N^s - 1
 * - R1 ≤ R2 ≤ R1 + 49
 * - C1 ≤ C2 ≤ C1 +49
 *
 * - 그래프 처럼 칸을 매번 만들면 공간 복잡도가 -> 10^8 = 100000000 => 메모리 초과
 *
 * # 풀이
 * - 그냥 시뮬레이션 하듯 다 만들어야할 것같은데 아 아니다
 * - N^S X N^S개 만들어두고, 분할 정복으로 색깔 채우기
 *
 * - 정사각형 덩어리 1개에서 시작
 * - 정사각형 덩어리 NXN개로 분할해가며 -> 색칠
 *
 */

import java.io.*;
public class BOJ1030_프렉탈평면 {
    static int s, N, K, R1, R2, C1, C2, ns;
    static int[][] result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        s = Integer.parseInt(temp[0]);
        N = Integer.parseInt(temp[1]);
        K = Integer.parseInt(temp[2]);
        R1 = Integer.parseInt(temp[3]);
        R2 = Integer.parseInt(temp[4]);
        C1 = Integer.parseInt(temp[5]);
        C2 = Integer.parseInt(temp[6]);

        ns = (int) Math.pow(N,s);
        result = new int[R2-R1+1][C2-C1+1];

        coloring(0,0, ns, 0);
        StringBuilder sb;
        for (int i=0; i < R2-R1+1; i++) {
            sb = new StringBuilder();
            for (int j=0; j < C2-C1+1; j++) {
                sb.append(result[i][j]);
            }
            System.out.println(sb);
        }
    }

    static void coloring(int sx, int sy, int len, int color) {
        if (sx > R2 || sy > C2 || sx+len <= R1 || sy+len <= C1)
            return;

        if (len == 1) {
            result[sx-R1][sy-C1] = color;
            return;
        }

        // 가운데 kxk 사각형 위치 구하기
        int new_len = len / N;
        int black = ((N - K) / 2) * new_len;

        // 가운데
        for (int i=0; i < len; i+=new_len) {
            for (int j=0; j<len; j+=new_len) {
                int new_color = color;
                if (i >= black && i < black+(K*new_len) && j >= black && j < black+(K*new_len)){
                    new_color = 1;
                }

                coloring(sx+i, sy+j, new_len, new_color);
            }
        }
    }
}
