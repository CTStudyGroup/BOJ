import java.io.BufferedReader;
import java.io.InputStreamReader;

/** BOJ2560_짚신벌레
 * # 문제
 * - 짚신벌레 특징
 *  - a번째 되는 날부터 새 개체 하나씩 만듬
 *  - b벤째 되는 날부터 새 개체를 만들지 않음.
 *  - d번째 되는 날 사망
 *
 * - 목표: N일째 되는 날 살아있는 짚신벌레 수
 * - 출력 형식: 목표%2
 *
 * # 제한
 * - 0＜a＜b＜d ≤ 10,000
 * - 1 ≤ N ≤ 1,000,000
 *
 * - 128MB -> 32백만개 int -> 다 만들면 메모리 초과가 날까?
 * - 1초 -> 1억번 -> 다 돌리면 시간 초과가 날까?
 *
 * - 수학적으로 계산해야할 것같음.
 *
 * # 풀이
 * - 배열을 하나 만들자 idx는 날짜로 쓰고 갚은 살아남은 벌레 수로 해서.
 * - 근데 동시에 번식가능한 수를 알아야지 추가할 수 있잖아. -> 이거 ㄴ앞에 수를 빼면 될 것도 같은데.
 * - 배열을 총 마리수 배열을 두고
 *  - 오늘 번식할 수는 (오늘-a 벌레수) - (오늘-b 벌레수)
 *  - 오늘 벌레 수는 (전날 벌레수 + 오늘 번식할 수)
 *  - 오늘, 사실은 사망해 있는 벌레 수는 오늘 벌레 수 - d일전 벌레수
 * -
 */

import java.io.*;
public class BOJ2560_짚신벌레 {
    public static void main(String[] args) throws IOException {
        // 기본 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a,b,d,N;
        String[] temp = br.readLine().split(" ");
        a = Integer.parseInt(temp[0]);
        b = Integer.parseInt(temp[1]);
        d = Integer.parseInt(temp[2]);
        N = Integer.parseInt(temp[3]);

        // 배열 생성 (0-N)
        int[] cnt = new int[N+1];
        cnt[0] = 1;

        // for문 돌리기 0부터 N+1 전까지
        for (int i = 1; i <= N; i++) {
            // list[i] = list[i-1] + (list[i-a] - list[i-b]) -> i-a랑 i-b 체크

            cnt[i] = cnt[i - 1];

            // 성체인 벌레수 만큼 +
            if (i-a >= 0) {
                cnt[i] = (cnt[i] + cnt[i - a]) % 1000;
            }

            // 더이상 번식 못하는 벌레 수만큼 -
            if (i-b >= 0) {
                cnt[i] = (cnt[i] - cnt[i - b] + 1000) % 1000;
            }

            cnt[i] %= 1000;
        }

        // 출력 list[N] - list[N-d] -> N-d 확인 / 나머지 연산
        if (N-d >= 0) {
            System.out.println((cnt[N] - cnt[N - d]+1000)%1000);
        } else {
            System.out.println(cnt[N]);
        }
    }
}
