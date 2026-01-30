import java.io.*;

/** BOJ9527_1의개수세기
 * # 문제
 * - A ≤ x ≤ B를 만족하는 모든 x에 대해 x를 이진수로 표현했을 때 1의 개수의 합
 *
 * # 제한
 * - 1초
 * - 128MB ->32백만개 int[10&16] 10000000000000000 -> 절대 안됨.
 * - 1 ≤ A ≤ B ≤ 10^16 -> long이나 String으로 받아야함.
 *
 * # 풀이
 * - dp로 풀면 될 것같은데
 * - 초기값을 [0, 1]로 세팅하고 2의 제곱수가 더해질 때 마다 2의 제곱수를 뺀 값을 가져오기..
 * - 크기가 안됨
 *
 * - 0000 0000
 * - 0001 0001
 *
 * - 0010 0011
 * - 0011 0022
 * - 0100 0122
 * - 0101 0223
 * - 0110 0333
 * - 0111 0444
 * - 1000 1444
 * - 1001 2445
 * - 1010 3455
 * - 1011 4466
 * - 1100 5566
 *
 * - 1101 6667
 * - 1110 7777
 * - 1111 8888
 *
 * 0 -> 01
 * 1 -> 0011
 * 2 -> 00001111
 * 3 -> 0000000011111111
 *
 * 0 -> (숫자 + 1) / 2
 * 1 -> (숫자
 *
 *
 * - 2^(자릿수)만큼 0과 1이 반복됨
 * - 숫자를 2*자릿수로 나눴을 때, 짝수 -> 0 홀수 -> 1
 * - 근데 어쨌든 이거 하나씩 하면, 시간 초과 나거든?
 * - 그러면,,, 판단 방법을 수직으로 바꿔보자
 * - 0에서 몇번,
 * - 1에서 몇번,, 이런식으로
 *
 * - 만약에 2-12면
 * - 2 -> 0 0 1 0
 * - 12 ->
 *
 */
public class BOJ9527_1의개수세기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long A, B, sumA=0, sumB=0;
        int cnt = 0;
        String[] temp = br.readLine().split(" ");
        A = Long.parseLong(temp[0]);
        B = Long.parseLong(temp[1]);

        long period, one, remain;

        // sumA: 0 ~ A
        while (1L << cnt <= (A-1)) {
            period = 1L << (cnt+1); // 0일 때 + 1일 때 -> 2배
            one = 1L << cnt;
            sumA += ((A-1+1)/period) * one;

            // 나머지
            remain = (A-1+1)%period;
            if (remain >= one) sumA += remain - one;

            cnt++;
        }

        // sumB: 0 ~ B
        cnt = 0;
        while (1L << cnt <= B) {
            period = 1L << (cnt+1); // 0일 때 + 1일 때 -> 2배
            one = 1L << cnt;
            sumB += ((B+1)/period) * one;

            // 나머지
            remain = (B+1)%period;
            if (remain >= one) sumB += remain - one;

            cnt++;
        }

        System.out.println(sumB-sumA);

    }
}
