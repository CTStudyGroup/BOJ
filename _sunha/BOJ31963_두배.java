/** BOJ31963_두배
 * # 문제
 * - 길이 N인 양의 정수열을 오름차순으로 만들기
 * - 각 수에 2를 곱할 수 있음
 * - 가장 적게 곱하는 횟수
 *
 * # 제한
 * - 1초
 * - 1024MB
 * - 1 ≤ N ≤ 250000
 * - 1 ≤ A_i ≤ 1000000 = 10^6
 * - 최악의 경우: 10^6, 10^6-1, ... , 10^6-N -> (10^6 - 250000) * 2^250000 ...?
 *
 * # 풀이
 * - 일단 생짜로 곱하는 건 안됨 뭐 BigInteger나 String 사용...
 * - 그리디하게하면 안되나? -> 그리디하게 하되 생짜로 안 곱하는 거지.
 *
 * - 2배 -> 비트연산? -> 걍 곱하기랑 비슷해서 굳이?
 *
 * - 기본 수 두고 곱해야하는 2의 개수 따로?
 * - 전체 곱해진 2의 개수, 바로 이전의 변형된 수, 현재 수 -> 이렇게 3개 알고 있으면 되니까.
 * - 바로 이전의 변형된 수 - 현재 수 -> 양수면 몫을 2로 나누고 나머지가 있으면 +1
 * - 계속 아래에서 계산하자
 *  - ((2^m)x - y) / 2 = n
 *  - 2^mx - y = 2n
 *  - x - y/2^m =
 *  - x/2 - y/2^(m+1) = n/2^m
 * - 근데 이러면 나머지 연산이 필요함...
 *
 */

//import java.io.*;
//import java.util.StringTokenizer;
//
//public class Main {
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st;
//        int[] nums;
//        int N, cnt=0, prevTwo=0, prev, now, diff, quoti, remain;
//
//        N = Integer.parseInt(br.readLine());
//
//        st = new StringTokenizer(br.readLine());
//        nums = new int[N];
//        for (int n=0; n<N; n++) {
//            nums[n] = Integer.parseInt(st.nextToken());
//        }
//
//        for (int n=1; n<N; n++) {
//            prev = nums[n-1];
//            now = nums[n]-1;    // 나머지 때문에
//
//            diff = prev - (now/(1 << prevTwo));
//            quoti = diff/2;
//            remain = diff%2;
//
//            if (quoti <= 0) prevTwo = 0;
//            else {
//                prevTwo = quoti * (1 << prevTwo);
//                if (remain > 0) prevTwo++;
//            }
//
//            cnt += prevTwo;
//        }
//        System.out.println(cnt);
//    }
//}

import java.io.*;
import java.util.StringTokenizer;

public class BOJ31963_두배 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        long totalOps = 0; // 전체 연산 횟수 (답)
        long currentMultipliers = 0; // 현재 수(A[i])에 누적된 2배 횟수

        for (int i = 1; i < N; i++) {
            // A[i-1] (이전 수)과 A[i] (현재 수)의 원본 크기 비교

            if (A[i-1] > A[i]) {
                // 현재 수가 더 작다면: 같거나 커질 때까지 2를 곱해야 함
                int count = 0;
                int temp = A[i];

                // A[i] * 2^count >= A[i-1]이 될 때까지 반복
                while (temp < A[i-1]) {
                    temp *= 2;
                    count++;
                }

                // 이전 수에 쌓여있던 횟수(currentMultipliers)에 + 이번에 필요한 횟수(count)
                currentMultipliers += count;

            } else {
                // 현재 수가 더 크다면: 이전 수의 누적 횟수보다 덜 곱해도 됨 (여유분 차감)
                int count = 0;
                int temp = A[i];
                int prevVal = A[i-1];

                // A[i]가 A[i-1]보다 2의 몇 승만큼 큰지 계산
                while (prevVal * 2 <= temp) {
                    prevVal *= 2;
                    count++;
                }

                // 여유분만큼 횟수를 줄임 (단, 0보다는 작아질 수 없음)
                currentMultipliers -= count;
                if (currentMultipliers < 0) {
                    currentMultipliers = 0;
                }
            }

            // 이번 위치(i)를 맞추기 위해 필요한 누적 횟수를 결과에 더함
            totalOps += currentMultipliers;
        }

        System.out.println(totalOps);
    }
}