import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        ArrayList<Integer> pos = new ArrayList<>(); // 오른쪽(양수)
        ArrayList<Integer> neg = new ArrayList<>(); // 왼쪽(음수, 절댓값으로 저장)

        int maxDist = 0;
        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(st.nextToken());
            if (x > 0) {
                pos.add(x);
                if (x > maxDist) maxDist = x;
            } else if (x < 0) {
                int a = -x;
                neg.add(a);
                if (a > maxDist) maxDist = a;
            }
        }

        // 내림차순 정렬 (먼 거리부터 처리)
        Collections.sort(pos, Collections.reverseOrder());
        Collections.sort(neg, Collections.reverseOrder());

        long ans = 0L;

        // 각쪽에서 M개씩 뽑을 때마다 2 * 거리 (왕복)
        for (int i = 0; i < pos.size(); i += M) {
            ans += 2L * pos.get(i);
        }
        for (int i = 0; i < neg.size(); i += M) {
            ans += 2L * neg.get(i);
        }

        // 전체에서 가장 먼 거리만큼 한 번만 가면 되므로 그만큼 빼줌
        ans -= maxDist;

        System.out.println(ans);
    }
}
