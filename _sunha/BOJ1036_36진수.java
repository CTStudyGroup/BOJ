///** BOJ_36진수
// * # 문제
// * - 36진법 숫자 N개에서 K개의 숫자를 고름 -> 전테에서 그 숫자를 Z로 변경 -> 다 더람
// * - 목적: 최댓값을 구하는 프로그램
// *
// * # 제한
// * - 2초
// * - 128MB
// * - N <= 50
// * - 수의 길이 <= 50
// * - 0 <= K <= 36
// *
// *
// * # 풀이
// * - 계산은 일단 ASCII - 55로 하고 비교
// * - 36진수 계산을 해보자. 나눠주면 되잖아. -> 이건 마지막에만,
// * - 그리디하게 풀까 완탐으로 풀까
// *  - 완탐 -> 36개에서 18개 고르기 -> 9,075,135,300 -> 절대 안됨
// * - 궁금한게 많이 등장하는 수 VS 가장 높은 수
// *
// * - 50개 중에서 가장 높은 자릿 숫자 pick
// * - 그 다음 자릿수 숫자 중에 pick하지 않은 숫자 pick
// * - 같은 자릿수가 있을 경우 더 작은 숫자부터 고르기
// * - 아니지 많이 등장하는게 나을 수도 있잖아. -> 같은 자릿수에서 많이 등장한거 먼저?
// *
// * - 와 이방법 말고 가중치 계산...!
// */
//import java.io.*;
//import java.util.Arrays;
//
//public class BOJ_36진수_main {
//    static String[] nums36;
//    static long[] nums10;
//    static long[] pick_weight = new long[36];
//    static int N,K;
//    static long original = 0, result;
//    static String base36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        N = Integer.parseInt(br.readLine());
//        nums36 = new String[N];
//        nums10 = new long[N];
//
//        for (int n=0; n<N; n++) {
//            nums36[n] = br.readLine();
//            original += convertTo10(nums36[n]);
//        }
//
//        K = Integer.parseInt(br.readLine());
//
//        // 모든 알파벳을 수정했을 때, 각각의 변화값.
//        for (int i=0; i<36; i++) {
//            char n = base36.charAt(i);
//            pick_weight[i] = -original;
//            for (String s: nums36) {
//                String new_num = s.replace(n, 'Z');
//                pick_weight[i] += convertTo10(new_num);
//            }
//        }
//        Arrays.sort(pick_weight);
//
//        result = original;
//        for (int k=0; k<K; k++) {
//            result += pick_weight[35-k];
//        }
//        System.out.println(Long.toString(result, 36).toUpperCase());
//    }
//
//    static long convertTo10(String num) {
//        long result = 0, o = 1;
//        for (int i=num.length()-1; i>=0; i--) {
//            char now = num.charAt(i);
//            if (now >= 65) result += (now - 55)*o;
//            else result += (now - '0')*o;
//            o*=36;
//        }
//        return result;
//    }
//}


/** BOJ_36진수
 * # 문제
 * - 36진법 숫자 N개에서 K개의 숫자를 고름 -> 전테에서 그 숫자를 Z로 변경 -> 다 더람
 * - 목적: "최댓값"을 구하는 프로그램
 *
 * # 제한
 * - 2초
 * - 128MB
 * - N <= 50
 * - 수의 길이 <= 50 -> 10진수로 계산한다면 36^50 -> 엄청 큰 수임 long으로도 불가(BigInteger 사용)
 * - 0 <= K <= 36
 *
 * # 풀이
 * 최댓값을 구하는 문제이기 때문에
 *
 * - input 받기
 * - 36개의 인덱스를 가지는 BigInteger 배열 생성
 * - 받은 36진수를 10진수로 바꾸어 sum 계산 -> original
 * - 주어진 문자열을 돌면서 BigInteger 배열에 Z-(해당 숫자)에 대한 값들을 누적해서 더람
 * - 그 중에 가장 큰 값 K개를 선택해서 original에 더하고 해당 값을 36진수로
 *
 */
import java.io.*;
import java.util.*;
import java.math.*;

public class BOJ1036_36진수 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N, K;
        BigInteger original = BigInteger.ZERO, result = BigInteger.ZERO;
        String[] nums;

        BigInteger[] weights = new BigInteger[36];
        for (int i = 0; i<36; i++) {
            weights[i] = BigInteger.ZERO;
        }

        N = Integer.parseInt(br.readLine());

        nums = new String[N];
        for (int n=0; n<N; n++) {
            nums[n] = br.readLine();
            String num36 = nums[n];
            BigInteger offset = BigInteger.ONE;
            for (int i=num36.length()-1; i>=0; i--) {
                char c36 = num36.charAt(i);
                int c10 = convertTo10(c36);

                original = original.add(BigInteger.valueOf(c10).multiply(offset));
                weights[c10] = weights[c10].add(BigInteger.valueOf(35 - c10).multiply(offset));

                offset = offset.multiply(BigInteger.valueOf(36));
            }
        }
        K = Integer.parseInt(br.readLine());

        Arrays.sort(weights, Collections.reverseOrder());

        for (int i=0; i<K; i++) {
            original = original.add(weights[i]);
        }
        System.out.println(original.toString(36).toUpperCase());

    }

    static int convertTo10(char c) {
        if (c >= 65) return c-'A' + 10;
        else return c-'0';
    }

}
