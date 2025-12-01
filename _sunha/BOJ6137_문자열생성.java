/** BOJ6137_문자열생성
 * # 문제
 * - N개의 문자로 이루어진 문자열 S -> 새로운 문자열 T
 * - 규칙
 *  - S 가장 앞을, T 마지막에 추가
 *  - S 가장 뒤를, T 마지막에 추가
 * - 목표: 사전 순으로 가장 빠른 문자열을 출력
 * - 출력 형식: 80글자마다 새줄 문자를 출력
 *
 * # 제한
 * - 1초
 * - 128MB
 * - N <= 2,000
 * -
 * # 풀이
 * - 양 쪽 중 더 작은 문자
 * - 같으면 그 안 쪽 걸로 비교
 * - 그리디?로 하면될 것같은데
 * - 비교를 위해 그냥 int로 받자(br.read()하면 int로 들어옴. 근데 newline 처리도 해줘야해서,,, 그냥 readline으로 받아와서 캐릭터 빼는게 나을 수도?)
 */

import java.io.*;
public class BOJ6137_문자열생성 {
    static int N;
    static char[] S;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        S = new char[N];

        for (int n=0; n<N; n++) {
            S[n] = br.readLine().charAt(0);
        }

        int lo = 0, hi = N-1;
        StringBuilder T = new StringBuilder(N);
        for (int n=0; n<N; n++) {
            if (n != 0 && n%80 == 0) T.append("\n");

            if (isLessThen(lo, hi)) T.append(S[lo++]);
            else T.append(S[hi--]);
        }
        System.out.println(T);
    }

    static boolean isLessThen(int lo, int hi) {
        if (lo >= hi) return true;

        if (S[lo] < S[hi]) return true;
        else if (S[lo] > S[hi]) return false;
        else return isLessThen(lo+1, hi-1);
    }
}
