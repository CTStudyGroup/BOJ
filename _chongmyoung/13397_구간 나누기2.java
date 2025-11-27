import java.util.*;
import java.io.*;

public class Main {

    static int N, M;
    static int[] arr;
  
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];
        st = new StringTokenizer(br.readLine());
        int max = 0, min = 10000;

      for(int i = 0; i < N; i++){
        arr[i] = Integer.parseInt(st.nextToken());
        max = Math.max(max, arr[i]);
        min = Math.min(min, arr[i]);
      }

      int left = 0;
      int right = max - min;
      int answer = right;

      while(left <= right) {
        int mid = (left + right) / 2;

        if(canDivide(mid)) {
          answer = mid;
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      }

      System.out.println(answer);
    }

    // mid를 점수 제한으로 했을 때 M개 이하로 구간 나누기 가능한지?
    static boolean canDivide(int mid) {
      int cnt = 1; // 구간 수
      int curMax = arr[0];
      int curMin = arr[0];

      for(int i = 1; i < N; i++){
        curMax = Math.max(curMax, arr[i]);
        curMin = Math.min(curMax, arr[i]);

        if(curMax - curMin > mid) {
          cnt++;
          curMax = arr[i];
          curMin = arr[i];
        }
      }

      return cnt <= M;
    }
}
