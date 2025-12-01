/** BOJ2632_피자판매
 * # 문제
 * - 여러 조각으로 나뉜 피자 A,B를 가지고 손님이 원하는 양을 판매
 * - 한 피자에서 2조각 이상을 파는 경우 연결해서 팔아야함.
 * - 목표: 판매하는 모든 방법의 가지 수 || 0
 *
 * # 제한
 * - 시간: 2초
 * - 메모리: 128MB
 *
 * - 구매할 크기 <= 2,000,000
 * - 3 ≤ m, n (조각 개수) ≤ 1000
 * - 1 ≤ (조각 크기) ≤ 1000
 *
 * # 풀이
 * - 모든 방법의 가지 수니까 완전탐색. -> 피자조각이 최대 1000인데 절대 안 될 것같은데 연결된 것만 가능이니까 되려나...?
 * - 7 1 2 2 2 -> 0 / 7 1 2 2 2 / 71 12 22 22 27 / 712 122 222 227 271 / 7122 1222 2227 2271 2712 / 71222
 * - 7 1 2 2 2 8 3 4 4 9 10 5 6 11 10 12 7 13 12 12 14
 * - 경우의 수가 2*(N(N-1) + 2) -> 대략 2000000
 * - 조합을 다 구하는 건 시간이 넘어가니까 필요한 값이 있는지 찾는 방법으로 -> 최대 A에서 하나 B에서 하나
 *
 * - 아 근데 저장 자체를 map 처럼 하면...! 훨씬 빠르겠는데?
 */

import java.io.*;

public class BOJ2632_피자판매 {
    static int order, M,N;
    static int[] pizza_m;
    static int[] pizza_n;
    static int[] size_cnt_m = new int[2000001];
    static int[] size_cnt_n = new int[2000001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        order = Integer.parseInt(br.readLine());
        String[] temp = br.readLine().split(" ");
        M = Integer.parseInt(temp[0]);
        N = Integer.parseInt(temp[1]);

        pizza_m = new int[M];
        pizza_n = new int[N];
        size_cnt_m[0] = 1;
        size_cnt_n[0] = 1;

        // 입력 받기 / 전체 합 구하기
        int all_m=0, all_n=0;
        for (int i = 0; i<M; i++) {
            pizza_m[i] = Integer.parseInt(br.readLine());
            all_m += pizza_m[i];
        }

        for (int i = 0; i<N; i++) {
            pizza_n[i] = Integer.parseInt(br.readLine());
            all_n += pizza_n[i];
        }

        // 가능한 조합의 합 구하기
        if (all_m <= order) size_cnt_m[all_m] = 1;
        if (all_n <= order) size_cnt_n[all_n] = 1;
        prefix_sum(pizza_m, size_cnt_m, M);
        prefix_sum(pizza_n, size_cnt_n, N);

        long result = 0; // 가짓수 구하는 문제는 long이 안전하다고함...
        for (int size = 0; size <= order; size++) {
            if (size_cnt_n[size] > 0) {
                result += (long) size_cnt_n[size]*size_cnt_m[order-size];
            }
        }
        System.out.println(result);
    }

    static void prefix_sum(int[] piece, int[] sum_cnt, int len) {
        // 조각이 2 ~ m-1(n-1) 개 일때 크기 저장
        int sum;
        for (int start = 0; start < len; start++) {
            sum = 0;
            for (int end = start; end < len+start-1; end++) {
                sum += piece[end%len];
                if (sum <= order) sum_cnt[sum]++;
                else break;
            }
        }
    }
}
