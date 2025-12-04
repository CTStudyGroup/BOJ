/** BOJ6987_월드컵
 * # 문제
 * - 동일한 조 국가끼리 한번씩 경기 치름
 * - 목적: 각 나라의 승, 무승부, 패의 수가 가능한 결과인지를 판별
 * - 출력 형식: 가능하면 1 불가능하면 0
 *
 * # 제한
 * - 1초
 * - 128MB
 *
 * # 풀이
 * - 체크해야하는 것
 *  - 간단
 *      - 각 국가의 경기 수가 5번인지
 *      - 각 조별로 승수 = 패수 인지
 *  - 복잡
 *      - 승일 경우 나를 제외하고 패 하나를 고름.
 *      - 패일 경우 나를 제외하고 승 하나를 고름.
 *      - 무승부일 경우 나를 제외하고 무승부 하나를 고름
 *      - 다 엮일 수 있는 조합이 있는지 확인
 *
 */

import java.io.*;
import java.util.*;

public class BOJ6987_월드컵 {
    static int[][] result = new int[6][3]; // 입력받은 결과 (승, 무, 패)
    static int[][] matches = new int[15][2]; // 15경기의 대진표 (팀1, 팀2)
    static boolean possible; // 가능한지 여부

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // 6개 팀의 대진표 생성 (총 15경기)
        int idx = 0;
        for (int i = 0; i < 6; i++) {
            for (int j = i + 1; j < 6; j++) {
                matches[idx][0] = i;
                matches[idx][1] = j;
                idx++;
            }
        }

        // 4가지 케이스 입력 및 처리
        for (int t = 0; t < 4; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int totalGame = 0;
            boolean basicCheck = true;

            for (int i = 0; i < 6; i++) {
                result[i][0] = Integer.parseInt(st.nextToken()); // 승
                result[i][1] = Integer.parseInt(st.nextToken()); // 무
                result[i][2] = Integer.parseInt(st.nextToken()); // 패

                // 간단한 체크: 한 팀의 경기 수는 무조건 5여야 함
                if (result[i][0] + result[i][1] + result[i][2] != 5) {
                    basicCheck = false;
                }
                totalGame += (result[i][0] + result[i][1] + result[i][2]);
            }

            // 간단한 체크: 전체 경기 승/무/패 합이 30이어야 함 (6팀 * 5경기)
            if (totalGame != 30 || !basicCheck) {
                sb.append(0).append(" ");
                continue;
            }

            possible = false;
            backtracking(0);

            if (possible) sb.append(1).append(" ");
            else sb.append(0).append(" ");
        }

        System.out.println(sb);
    }

    static void backtracking(int matchIdx) {
        if (possible) return; // 이미 가능한 경우를 찾았으면 더 탐색 안 함

        // 15경기를 모두 다 치른 경우
        if (matchIdx == 15) {
            possible = true;
            return;
        }

        int team1 = matches[matchIdx][0];
        int team2 = matches[matchIdx][1];

        // 1. Team1 승리 (Team2 패배)
        if (result[team1][0] > 0 && result[team2][2] > 0) {
            result[team1][0]--;
            result[team2][2]--;
            backtracking(matchIdx + 1);
            result[team1][0]++;
            result[team2][2]++;
        }

        // 2. 무승부 (Team1 무, Team2 무)
        if (result[team1][1] > 0 && result[team2][1] > 0) {
            result[team1][1]--;
            result[team2][1]--;
            backtracking(matchIdx + 1);
            result[team1][1]++;
            result[team2][1]++;
        }

        // 3. Team1 패배 (Team2 승리)
        if (result[team1][2] > 0 && result[team2][0] > 0) {
            result[team1][2]--;
            result[team2][0]--;
            backtracking(matchIdx + 1);
            result[team1][2]++;
            result[team2][0]++;
        }
    }
}
