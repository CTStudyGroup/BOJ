import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    // 노드 정보를 저장할 클래스 (굳이 클래스 없이 2차원 배열로도 가능하지만 가독성을 위해 사용)
    static class Node {
        int left;
        int right;

        public Node(int left, int right) {
            this.left = left;
            this.right = right;
        }
    }

    static Node[] tree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 1. 노드 개수 입력
        int N = Integer.parseInt(br.readLine());
        
        // 노드 번호는 1부터 N까지이므로 N + 1 크기로 할당
        tree = new Node[N + 1];

        // 2. 트리 정보 입력
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int root = Integer.parseInt(st.nextToken());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());

            tree[root] = new Node(left, right);
        }

        // 3. 루트(1번)부터 오른쪽 방향으로만 이동하며 거리(depth) 측정
        int rightSpineCount = 0;
        int current = 1;

        while (true) {
            int rightChild = tree[current].right;
            
            if (rightChild != -1) {
                rightSpineCount++;
                current = rightChild;
            } else {
                break; // 더 이상 오른쪽 자식이 없으면 종료
            }
        }

        // 4. 공식 적용
        // 전체 왕복 이동 횟수 = 2 * (N - 1)
        // 정답 = 전체 왕복 - 오른쪽 끝까지 내려가는 경로(되돌아오지 않음)
        int totalEdges = N - 1;
        int result = 2 * totalEdges - rightSpineCount;

        System.out.println(result);
    }
}
