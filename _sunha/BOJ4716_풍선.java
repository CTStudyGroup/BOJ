import java.io.*;
import java.util.Arrays;

/** BOJ4716_풍선
 * # 문제
 *
 * - 입력: 여러개의 테케 / 마지막줄 0 0 0
 * - 이동거리 최솟값을 하나씩 출력
 *
 * # 제한
 * - 1초
 * - 128MB
 * - 팀 수: 1 ≤ N ≤ 1,000
 * - 풍선수: 0 ≤ A, B ≤ 10,000
 * - 거리: 0 ≤ DA, DB ≤ 1,000
 *
 * # 풀이
 * - 각 팀의 이동 가중치를 체크: (A-B) * 풍선개수
 * - 아니지 팀마다 다른 풍선 개수를 가지고 있을 수도 있잖아?
 *
 */

public class BOJ4716_풍선 {

  static int N, result;
  static int[] cnt = new int[3];
  static int[][] teams, weight;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] temp;

    temp = br.readLine().split(" ");
    cnt[0] = Integer.parseInt(temp[0]);  //N
    cnt[1] = Integer.parseInt(temp[1]);  //A
    cnt[2] = Integer.parseInt(temp[2]);  //B
    N = cnt[0];

    while (cnt[0] != 0 || cnt[1] != 0 || cnt[2] != 0) {
      result=0;
      teams = new int[N][3]; // 풍선수, da, db
      weight = new int[N][4]; // 가중치, 더 가까운 방, index

      // 배열 채우기
      for (int n=0; n<N; n++) {
        temp = br.readLine().split(" ");
        teams[n][0] = Integer.parseInt(temp[0]);
        teams[n][1] = Integer.parseInt(temp[1]);
        teams[n][2] = Integer.parseInt(temp[2]);

        if (teams[n][1] < teams[n][2]) {
          weight[n][0] = teams[n][2] - teams[n][1];
          weight[n][1] = 1;
          weight[n][2] = 2;
        }
        else {
          weight[n][0] = teams[n][1] - teams[n][2];
          weight[n][1] = 2;
          weight[n][2] = 1;
        }
        weight[n][3] = n;
      }

      // 최소값
      // 가중치 정렬
      Arrays.sort(weight, (o1, o2) -> (o2[0] - o1[0]));

      for (int[] t: weight) {
        int near = t[1];
        int far = t[2];
        int i = t[3];
        int k = teams[i][0];
        int lenNear = teams[i][near];
        int lenFar = teams[i][far];

        if (cnt[near] > k) {
          result += lenNear * k;
          cnt[near] -= k;
        }
        else {
          result += (lenFar * (k-cnt[near])) + (lenNear * cnt[near]);
          cnt[far] -= (k-cnt[near]);
          cnt[near] = 0;
        }
      }

      System.out.println(result);


      // 다음 테케
      temp = br.readLine().split(" ");
      cnt[0] = Integer.parseInt(temp[0]);  //N
      cnt[1] = Integer.parseInt(temp[1]);  //A
      cnt[2] = Integer.parseInt(temp[2]);  //B
      N = cnt[0];
    }
  }
}
