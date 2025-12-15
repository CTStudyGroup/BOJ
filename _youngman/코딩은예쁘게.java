package 백준;

import java.io.*;
import java.util.*;

public class 코딩은예쁘게 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N=Integer.parseInt(st.nextToken());
        int[] change = new int[N];
        int[] fix = new int[N];
        int[] diff = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            change[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            fix[i] = Integer.parseInt(st.nextToken());
            diff[i] = change[i] - fix[i];
        }

        // 첫 번째 값
        int answer = Math.abs(diff[0]);

        for (int i = 1; i < N; i++) {
            // 같은 부호일 때만 증가분을 계산 -> 마이너스끼리 곱하면 0보다 크고 양수끼리 곱해도 0보다 크니깐
            if (diff[i] * diff[i - 1] > 0) {
                answer += Math.max(0, Math.abs(diff[i]) - Math.abs(diff[i - 1]));
            } else {
                // 부호가 바뀌면 새로 시작
                answer += Math.abs(diff[i]);
            }
        }

        System.out.println(answer);

    }
}
