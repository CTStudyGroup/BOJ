/** BOJ1461_도서관
 * # 문제
 * - 목표: 책을 다 되돌려놓는 최소거리 구하기
 * - 조건: 한번에 책을 M권씩만 들 수 있음.
 *
 * # 제한
 * - 2초
 * - 128MB
 * - 1 <= N(전체 책), M(들 수 있는 수) <= 50
 * - 1 <= abs(위치) <= 10000
 *
 * # 풀이
 * - 일단 위치 값이 1개씩 들어오는 거 보니까 그래프는 아닌 거 같은데
 *
 * - 조건 M을 기준으로 생각해보면
 * - M이 1일 때 최단 경로: (모든 위치값 * 2) - 제일 짧은 값
 * - M이 2일 때 최단 경로:
 * - DP도 애매하고
 *
 * - 마지막에 어디를 갈까. -> 제일 먼곳
 * - 마지막에 갈 곳을 미리 빼고
 * - 나머지를 일반 적으로 처리하자
 *
 * - 자료구조: 음수 배열, 양수 배열 -> 정렬
 * - 최댓값있는 배열에서 큰 차례로 M만큼 선택 -> 마지막 갈 곳
 * - 큰 값부터 M만큼 선택후 그 중 (최댓값 *2) 를 결과에 더람
 * - 마지막 갈 곳의 최댓갑을 결과에 더함
 */

import java.io.*;
import java.util.*;

public class BOJ1461_도서관 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N,M, result = 0;
        ArrayList<Integer> plus = new ArrayList<>();
        ArrayList<Integer> minus = new ArrayList<>();

        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);

        StringTokenizer st = new StringTokenizer(br.readLine());
        int num;
        for (int n=0; n<N; n++) {
            num = Integer.parseInt(st.nextToken());
            if (num < 0) minus.add(Math.abs(num));
            else plus.add(num);
        }

        // 역순 정렬
        Collections.sort(plus, (o1, o2) -> o2- o1);
        Collections.sort(minus, (o1, o2) -> o2- o1);


        // 마지막에 놓을 책 결정.
        int pi=0, mi=0;

        // plus0이랑 minus0이랑 비교
        // plus0이 더 크면
        // 없는 경우도 체크해야함.
        int max_plus = !plus.isEmpty() ? plus.get(0) : 0;
        int max_minus = !minus.isEmpty() ? minus.get(0) : 0;

        if (max_plus > max_minus){
            // M만큼 idx를 이동하고
            pi = M;
            // result에 plus0의 값을 더함
            result += max_plus;
        }
        // minus0이랑 더 크면
        else {
            // M만큼 idx를 이동하고
            mi = M;
            // result에 minus0이랑 값을 더함
            result += max_minus;
        }


        // 나머지 경로 체크
        // plus
        while (pi < plus.size()) {
            // idx가 plus size보다 작은 동안 까지 반복
            // idx를 M씩 이동하면서 최댓값 * 2를 더함
            result += plus.get(pi)*2;
            pi += M;
        }

        // minus
        while (mi < minus.size()) {
            // idx가 plus size보다 작은 동안 까지 반복
            // idx를 M씩 이동하면서 최댓값 * 2를 더함
            result += minus.get(mi) * 2;
            mi += M;
        }

        System.out.println(result);
    }
}
