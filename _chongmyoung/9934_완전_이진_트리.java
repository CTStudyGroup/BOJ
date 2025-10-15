import java.io.*;
import java.util.*;

public class Main {
    static int K;
    static int[] arr;
    static List<Integer>[] levels;

    // 중위 순회 방식으로 트리 구성
    static void buildTree(int start, int end, int depth) {
        if (start > end || depth >= K) return;

        int mid = (start + end) / 2;
        levels[depth].add(arr[mid]);

        buildTree(start, mid - 1, depth + 1);
        buildTree(mid + 1, end, depth + 1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());
        arr = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        levels = new ArrayList[K];
        for (int i = 0; i < K; i++) {
            levels[i] = new ArrayList<>();
        }

        buildTree(0, arr.length - 1, 0);

        // 각 레벨의 노드 출력
        for (int i = 0; i < K; i++) {
            System.out.println(String.join(" ", levels[i].stream()
                                                      .map(String::valueOf)
                                                      .toArray(String[]::new)));
        }
    }
}
