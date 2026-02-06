import java.io.*;
import java.util.*;

public class Main {

    static class Brick {
        int area, height, weight, idx;
        Brick(int area, int height, int weight, int idx) {
            this.area = area;
            this.height = height;
            this.weight = weight;
            this.idx = idx;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Brick[] bricks = new Brick[N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int area = Integer.parseInt(st.nextToken());
            int height = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            bricks[i] = new Brick(area, height, weight, i + 1);
        }

        // 1. 밑면 넓이 내림차순 정렬
        Arrays.sort(bricks, (a, b) -> b.area - a.area);

        int[] dp = new int[N];
        int[] prev = new int[N];
        Arrays.fill(prev, -1);

        int maxHeight = 0;
        int lastIdx = 0;

        // 2. DP
        for (int i = 0; i < N; i++) {
            dp[i] = bricks[i].height;
            for (int j = 0; j < i; j++) {
                if (bricks[j].weight > bricks[i].weight) {
                    if (dp[j] + bricks[i].height > dp[i]) {
                        dp[i] = dp[j] + bricks[i].height;
                        prev[i] = j;
                    }
                }
            }
            if (dp[i] > maxHeight) {
                maxHeight = dp[i];
                lastIdx = i;
            }
        }

        // 3. 역추적
        List<Integer> result = new ArrayList<>();
        while (lastIdx != -1) {
            result.add(bricks[lastIdx].idx);
            lastIdx = prev[lastIdx];
        }

        // 출력
        System.out.println(result.size());
        for (int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));
        }
    }
}
