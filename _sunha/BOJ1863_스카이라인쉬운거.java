import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

/**
 * # 문제
 * 스카이 라인을 보고 최소 건물 수 알아내기.
 *
 * # 제한
 * - 변수 범위: int 가능
 *      - n(고도 바뀌는 지점 개수) <= 50,000 개
 *      - 1 <= x <= 1,000,000
 *      - 0 <= y <= 500,000
 * - 시간: 2초 -> 2억번
 * - 공간: 128MB -> 32백만개 int
 *
 * # 해결
 * - 히스토그램 문제 처럼?
 * - 위에서 부터 내려오기?
 * 1. stack에 높이 넣기
 * 2. top > now면,
 *      2-1. top <= now 일때까지 pop
 *      2-2. pop하면서 conut 올리기 (0인경우 제외)
 * 3. 동일한 높이가 아닌 경우 stk에 넣기
 * - 0 1 1 2 2
 */

import java.io.*;
import java.util.*;

public class BOJ1863_스카이라인쉬운거 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Deque<Integer> stk = new ArrayDeque<>();
        int result = 0;

        // buildings 배열 만들기
        String[] temp;
        int newHeight, now;
        for (int n=0; n<N; n++) {
            temp = br.readLine().split(" ");
            newHeight = Integer.parseInt(temp[1]);

            // top <= now 일때까지 pop
            while (!stk.isEmpty() && stk.peekLast() > newHeight) {
                stk.pollLast();
                result += 1;
            }

            if (!stk.isEmpty() && stk.peekLast() == newHeight) {
                continue;
            }

            stk.offer(newHeight);

        }

        while (!stk.isEmpty()) {
            now = stk.pollLast();
            if (now != 0) {
                result += 1;
            }
        }
        System.out.println(result);
    }
}