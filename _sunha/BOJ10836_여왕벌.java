/** BOJ10836_여왕벌
 * # 문제
 * - 목적: 마지막 날 저녁의 애벌레들의 크기
 * - "이 값들은 감소하지 않는다?"
 * - 그 날 가장 많이 자란 애벌레가 자란 만큼
 *  - 오른쪽으로 갈때는,
 *
 * # 제한
 * - 2초
 * - 256MB
 * - 2 ≤ M(가로,세로) ≤ 700
 * - 1 ≤ N(날짜수) ≤ 1,000,000
 * - 0 ≤ 하루동안 자라는 정도 ≤ 2
 *
 * - int 안에 가능할듯?
 * - 매일 490000 이면 시간 훌쩍 넘음.
 * - 뭉갤 건 뭉개야함
 *
 * # 풀이
 * - 뭉갤 부분이
 * - 제일 오른쪽 열 -> 가장 윗 행과 동일함.
 * - 그냥 입력값 처리만 계속 해주고 마지막에 채우기
 * - 근데 입력값을 받아서 모서리 하나하나를 처리하는 건 그자체로 시간초과임 -> (2M-1)*N = 최악의 경우 1399000000....
 * - 차분 배열이라는 걸 사용해야함...
 *
 *
 */

import java.io.*;
import java.util.*;

public class BOJ10836_여왕벌 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int M,N;
        int[] diff;

        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        diff = new int[M*2-1];  // 변화량

        // N개 돌면서 입력받기
        int zero, one, two;
        for (int n=0; n<N; n++) {
            st = new StringTokenizer(br.readLine());
            zero = Integer.parseInt(st.nextToken());
            one = Integer.parseInt(st.nextToken());
//            two = Integer.parseInt(st.nextToken());

            // 각각의 위치에 차수 더하기. +1/ +2
            if (zero < diff.length) diff[zero] += 1;
            if (zero+one < diff.length) diff[zero + one] += 1;
        }

        for (int i = 1; i< diff.length; i++) {
            diff[i] += diff[i-1];
        }


        StringBuilder sb = new StringBuilder();
        for (int i=0; i<M; i++) {
            sb.append(1 + diff[M-1-i]);
            for (int j=0; j<M-1; j++) {
                sb.append(" " + (1+diff[M+j]));
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
