import java.io.*;

/** BOJ11049_행렬곱셈순서
 * # 문제
 * -
 * - 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값

 * # 제한
 * - 1초
 * - 256MB
 * - 최악의 경우 = 2^31 - 1 -> Int 사용
 *
 * # 풀이
 * - DP 로하면 될 것같은데?
 * dp(idx) = idx 까지 곱했을 때, 최소값 (실패)
 *
 * top-down 방식으로
 * dp(s,e) = s ~ e까지의 최소값
 *  = max(dp(s,e-i) + dp(e-i,s)) (s <= i <= e)
 *
 */

public class BOJ11049_행렬곱셈순서 {

  static int N;
  static int[][] nums, dp;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] temp;

    N = Integer.parseInt(br.readLine());
    nums = new int[N][2];
    dp = new int[N][N];

    // 초기값
    for (int n = 0; n < N; n++) {
      temp = br.readLine().split(" ");
      nums[n][0] = Integer.parseInt(temp[0]);
      nums[n][1] = Integer.parseInt(temp[1]);
      for (int m = 0; m < N; m++) {
        dp[n][m] = -1;
      }
    }
    System.out.println(findMax(0,N-1));
  }

  static int findMax(int si, int ei) {
    if (dp[si][ei] != -1) return dp[si][ei];

    dp[si][ei] = Integer.MAX_VALUE;
    if (si == ei) dp[si][ei] = 0;
    else if (si+1 == ei) dp[si][ei] = nums[si][0] * nums[si][1] * nums[ei][1];
    else {
      for (int i = si; i < ei; i++) {
        dp[si][ei] = Math.min(
            findMax(si, i) + findMax(i + 1, ei) + (nums[si][0] * nums[i][1] * nums[ei][1]),
            dp[si][ei]);
      }
    }

    return dp[si][ei];
  }
}
