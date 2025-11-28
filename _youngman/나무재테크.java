import java.io.*;
import java.util.*;

public class Main {

    static int N, M, K;
    static int[][] add;       // 겨울에 더해지는 양분
    static int[][] food;      // 현재 양분
    static List<Integer>[][] tree; // 각 칸에 있는 나무들의 나이

    static int[] dy = {-1,-1,0,1,1,1,0,-1};
    static int[] dx = {0,1,1,1,0,-1,-1,-1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        add = new int[N][N];
        food = new int[N][N];
        tree = new ArrayList[N][N];

        // 초기값 넣기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                tree[i][j] = new ArrayList<>();
                food[i][j] = 5; // 기본 양분 5
            }
        }

        // 겨울에 추가되는 양분
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                add[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 초기 나무 입력
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken()) - 1;
            int x = Integer.parseInt(st.nextToken()) - 1;
            int age = Integer.parseInt(st.nextToken());
            tree[y][x].add(age);
        }

        // K년 동안 사계절 반복
        while (K-- > 0) {
            springSummer();
            fall();
            winter();
        }

        // 살아있는 나무 수 계산
        int answer = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                answer += tree[i][j].size();
            }
        }

        System.out.println(answer);
    }

    // 봄 + 여름
    static void springSummer() {
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {

                if (tree[y][x].size() == 0) continue;

                List<Integer> list = tree[y][x];
                Collections.sort(list);  // 어린 나무부터 양분 먹임

                List<Integer> newList = new ArrayList<>();
                int deadFood = 0;

                for (int age : list) {
                    if (food[y][x] >= age) { // 양분 먹고 성장
                        food[y][x] -= age;
                        newList.add(age + 1);
                    } else {
                        deadFood += age / 2;  // 죽어서 양분이 됨
                    }
                }

                food[y][x] += deadFood;
                tree[y][x] = newList; // 살아남은 나무만 저장
            }
        }
    }

    // 가을: 번식
    static void fall() {
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {

                for (int age : tree[y][x]) {
                    if (age % 5 == 0) {
                        for (int d = 0; d < 8; d++) {
                            int ny = y + dy[d];
                            int nx = x + dx[d];

                            if (ny < 0 || nx < 0 || ny >= N || nx >= N) continue;

                            // 어린 나무는 리스트 맨 앞에 넣어야 나중에 정렬 비용 감소
                            tree[ny][nx].add(0, 1);
                        }
                    }
                }

            }
        }
    }

    // 겨울: 양분 추가
    static void winter() {
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < N; x++) {
                food[y][x] += add[y][x];
            }
        }
    }
}
