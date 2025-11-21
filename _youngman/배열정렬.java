
import java.io.*;
import java.util.*;

public class 배열정렬 {
    static int N, M;
    static int[][] operations;
    static HashMap<String, Integer> dist;
    static int[] targetArr;
    static String targetState;

    static class Node implements Comparable<Node> {
        String state;
        int cost;

        public Node(String state, int cost) {
            this.state = state;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.cost, other.cost);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        int[] initialArr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            initialArr[i] = Integer.parseInt(st.nextToken());
        }

        M = Integer.parseInt(br.readLine());
        operations = new int[M][3];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            operations[i][0] = Integer.parseInt(st.nextToken()) - 1;
            operations[i][1] = Integer.parseInt(st.nextToken()) - 1;
            operations[i][2] = Integer.parseInt(st.nextToken());
        }

        // 4. 목표 상태 설정 (수정된 converter 사용)
        targetArr = initialArr.clone();
        Arrays.sort(targetArr);
        targetState = converter(targetArr);

        // 5. 다익스트라 실행 및 결과 출력
        int minCost = dijkstra(initialArr);

        System.out.println(minCost == Integer.MAX_VALUE ? -1 : minCost);
    }

    /**
     * 배열 상태를 하나의 문자열로 변환합니다. (구분자 추가)
     */
    public static String converter(int[] arr) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i]);
            if (i < arr.length - 1) {
                sb.append(","); // 콤마(,)로 구분하여 10 이상 숫자 처리
            }
        }
        return sb.toString();
    }

    /**
     * 문자열 상태를 배열로 변환합니다. (구분자로 분리)
     */
    public static int[] deconverter(String state) {
        String[] parts = state.split(","); // 콤마(,) 기준으로 분리
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(parts[i]); // 문자열을 정수로 변환
        }
        return arr;
    }


    /**
     * 다익스트라 알고리즘을 사용하여 최소 비용을 계산합니다. (로직은 동일)
     */
    public static int dijkstra(int[] initialArr) {
        dist = new HashMap<>();
        PriorityQueue<Node> pq = new PriorityQueue<>();

        String initialState = converter(initialArr);
        dist.put(initialState, 0);
        pq.offer(new Node(initialState, 0));

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            String currentState = current.state;
            int currentCost = current.cost;

            if (currentState.equals(targetState)) {
                return currentCost;
            }
            if (currentCost > dist.getOrDefault(currentState, Integer.MAX_VALUE)) {
                continue;
            }

            // 현재 상태를 배열로 변환
            int[] currentArr = deconverter(currentState);

            for (int i = 0; i < M; i++) {
                int idx1 = operations[i][0];
                int idx2 = operations[i][1];
                int opCost = operations[i][2];

                int[] nextArr = currentArr.clone();

                // 조작 수행 (교환)
                int temp = nextArr[idx1];
                nextArr[idx1] = nextArr[idx2];
                nextArr[idx2] = temp;

                String nextState = converter(nextArr);
                int nextCost = currentCost + opCost;

                if (nextCost < dist.getOrDefault(nextState, Integer.MAX_VALUE)) {
                    dist.put(nextState, nextCost);
                    pq.offer(new Node(nextState, nextCost));
                }
            }
        }

        return Integer.MAX_VALUE;
    }
}