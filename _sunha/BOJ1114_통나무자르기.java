/** BOJ1114_통나무자르기
 * # 문제
 * - 목적: 나무의 긴조각을 작게만들기 -> 최대한 평균에 맞게 자르기..
 * - 출력형식: (가장 긴 조각의 길이) (처음 자르는 위치 -> 작은 순)
 *
 * # 제한
 * - 2초
 * - 128MB
 * - 2 ≤ L ≤ 1,000,000,000
 * - 1 ≤ K, C ≤ 10,000
 * - 1 ≤ 자를 수 있는 위치 ≤ L
 *
 * - 완탐은 절대 아님
 *
 * # 풀이
 * - 아마 이분탐색을 쓰지 않을까?
 * - 평균에 가깝게 잘라야하잖아?
 * - 그러면 평균보다 하나 위의 값까지 선택가능하게? 아니다 왼쪽기준이니까 하나 아래의 값을 선택하면,
 *
 * - 아 고급 이분탐색에서 자주나오는 패턴으로: 가장 긴 나무 조각의 값을 이분탐색하는식?
 * - 오른쪽에서부터 그길이만큼 자를 수 있는지 체크 -> 일단 되는 걸로만 하는 걸로 하자 index 기준으로 탐색
 * - 자를 수 있다면 나머지 부분에서 그 길이 이하로, c-1번(2) 자를 수 있는지 체크
 * - 그 길이 이하로 자를 수 없다면, 탐색 범위를 왼쪽으로 좁힘
 * - c-1번 자를 수 없다면, 탐색범위를 오른쪽으로 좁힘
 *
 *
 */

import java.io.*;
import java.util.*;

public class BOJ1114_통나무자르기 {
    static int L, K, C;
    static List<Integer> tree;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        // 중복 제거용
        Set<Integer> temp = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i<K; i++) {
            temp.add(Integer.parseInt(st.nextToken()));
        }
        tree = new ArrayList<>(temp);
        tree.add(0);
        tree.add(L);
        Collections.sort(tree, Collections.reverseOrder());


        // 모든 간격(gap) 중 최댓값을 구함
        int max_gap = 0;
        for (int i=1; i< tree.size(); i++) {
            max_gap = Math.max(max_gap, tree.get(i-1) - tree.get(i));
        }

        int lo = max_gap, hi = L, mid, prev = 0;
        int result = -1, first = -1, cnt;

        while (lo < hi) {
            mid = (hi+lo)/2;
            prev = L;
            cnt = 0;

            for (int i=0; i<tree.size(); i++) {
                if (prev - tree.get(i) > mid) {
                    cnt++;
                    prev = tree.get(i-1);
                }
            }

            if (cnt <= C) {  // 간격이 넚거나 같음 -> 가능하니까 줄여봄
                hi = mid;
                if (cnt == C) first = prev;
                else first = tree.get(tree.size()-2);
            } else {        // 불가능 하니까 늘림
                lo = mid+1;
            }
        }

        System.out.println(lo + " " + first);
    }
}
