/** BOJ1082_방번호
 *
 * 7:15
 *
 * # 문제
 * - 목표: M원을 이용해서 만들 수 있는 가장 큰 방번호
 * - 파는 숫자: 0 ~ N-1
 * - 각 숫자는 무한히 구매할 수 있다.
 *
 * # 제한
 * - 2초 = 2억번
 * - 128MB
 * - 입력
 *  - 1 ≤ N ≤ 10
 *  - 1 ≤ Pi ≤ 50
 *  - 1 ≤ M ≤ 50
 *
 * # 풀이
 * - 그리디 하게 하면 안되나?
 * - 일단 1차적으로 구매하는 숫자의 개수가 가장 중요하고
 * - 2차적으로는 큰 수부터 구매하는게 중요한데
 * - 가치판단하기 힘드니까 그리디는 빼고
 * - 숫자가 적어서 백트래킹 써도 될듯? -> 아니 무한히 구매할 수 있어서 절대 안됨
 * - 아니면 DP? -> DP는 금액 기준으로 해야할 것같은데.
 *  - dp[수][돈] = max(int(str(수) + str(max(dp[수-1][돈-수의 가격])), dp[수][돈-수의 가격])), dp[수-1][돈])
 *
 */
//import java.io.*;
//import java.util.Arrays;
//
//public class Main {
//
//    public static void main(String[] args) throws IOException {
//
//        // Data
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int N, M, result = 0;
//        String[] temp;
//        int[] P;
//        String[][] dp;
//
//        N = Integer.parseInt(br.readLine());
//
//        P = new int[N];
//        temp = br.readLine().split(" ");
//        for (int n = 0; n<N; n++) {
//            P[n] = Integer.parseInt(temp[n]);
//        }
//
//        M = Integer.parseInt(br.readLine());
//
//        dp = new String[N][M+1];
//
//        // n=0일 때 초기화
//        for (int m = 0; m<=M; m++) {
//            dp[0][m] = "0".repeat(m/P[0]);
//        }
//
//        for (int n = 1; n<N; n++) {
//            for (int m = 0; m<=M; m++) {
//                String c1 = "",c2;
//                // '숫자 n' o
//                if (m-P[n] >= 0) c1 = maxString(n + dp[n - 1][m - P[n]], n + dp[n][m - P[n]]);
//
//                // '숫자 n' x
//                c2 = dp[n-1][m];
//
//                dp[n][m] = maxString(c1, c2);
//            }
//        }
//        for (int n = 0; n<N; n++) {
//            System.out.println(Arrays.toString(dp[n]));
//        }
//        if (dp[N-1][M].startsWith("00")) System.out.println("0");
//        else System.out.println(dp[N-1][M]);
//    }
//
//    static String maxString(String a, String b) {
//        if (a.startsWith("00")) a = "0";
//        if (b.startsWith("00")) b = "0";
//
//        if (a.length() > b.length()) return a;
//        else if (a.length() < b.length()) return b;
//        else {
//            if (a.compareTo(b) > 0) return a;
//            else return b;
//        }
//    }
//}

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class number{
    int num, price;
    number(int num, int price) {this.num = num; this.price = price;}
}

public class BOJ1082_방번호 {
    private static int N, pocket;
    private static int res[] = new int[100];
    private static number arr[];
    private static Map<Integer, Integer> m = new HashMap<>(); // 숫자-비용 따로 저장해두려고

    public static void main(String[ ] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt(); arr = new number[N];
        for(int i = 0; i < N; i++) {
            arr[i] = new number(i, sc.nextInt());
            m.put(i, arr[i].price);
        }
        pocket = sc.nextInt();

        Arrays.sort(arr, new Comparator<number>() { // 가격 기준 오름차순 정렬
            @Override
            public int compare(number o1, number o2) {
                if(o1.price == o2.price) return o1.num - o2.num;
                return o1.price - o2.price;
            }

        });

        int cnt = 0;
        if(arr[0].num == 0) { // 숫자 0이 가장 작은 수라서 맨 앞에 올 수 없기 때문에
            if(N == 1 || arr[1].price > pocket) { // 0대신 넣을 그 다음 숫자의 비용을 감당할 수 없다면
                System.out.println(0); // 숫자 0으로밖에 할 수 없을 때 답은 0
                System.exit(0);
            }
            res[cnt++] = arr[1].num; // 그 다음 숫자의 비용을 감당할 수 있으면 이 숫자로 맨 앞자리 채운다
            pocket -= arr[1].price;
        }

        while(pocket - arr[0].price >= 0) { // 가장 비용이 작은 숫자로 최대한 많이 채움
            res[cnt++] = arr[0].num;
            pocket -= arr[0].price;
        }

        for(int i = 0; i < cnt; i++) {
            for(int j = N - 1; j >= 0; j--) { // 가장 큰 수부터
                if(i == 0 && j == 0) continue; // 맨 앞자리에 0이 들어가면 안 됨
                int tmp = pocket + m.get(res[i]) - m.get(j);
                if(tmp >= 0) { // 가격 범위 안 넘어서 현재 숫자로 바꿀 수 있으면 바꿈(최대한 큰 수이므로)
                    pocket = tmp; // 허용 가능한 비용 갱신
                    res[i] = j;
                    break;
                }
            }
        }

        for(int i = 0; i < cnt; i++) System.out.print(res[i]);
    }
}