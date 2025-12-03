import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, M, T;
    static int[][] map; // 원판 상태 저장 (1번 원판 ~ N번 원판)

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken()); // 원판의 크기
        M = Integer.parseInt(st.nextToken()); // 숫자의 개수
        T = Integer.parseInt(st.nextToken()); // 명령 횟수

        map = new int[N + 1][M]; // 1번 인덱스부터 사용하기 위해 N+1

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // T번의 명령 수행
        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()); // x의 배수 원판
            int d = Integer.parseInt(st.nextToken()); // 방향 (0: 시계, 1: 반시계)
            int k = Integer.parseInt(st.nextToken()); // 회전 칸 수

            // 1. 회전
            rotateDisks(x, d, k);

            // 2. 인접한 수 찾기 및 처리
            // 반환값이 false면 지워진 수가 없다는 뜻 -> 평균 처리 로직 실행
            if (!removeAdjacent()) {
                adjustByAverage();
            }
        }

        // 최종 합 계산
        System.out.println(calculateSum());
    }

    // 원판 회전 메서드
    static void rotateDisks(int x, int d, int k) {
        // x의 배수인 원판들을 회전
        for (int i = x; i <= N; i += x) {
            int[] temp = new int[M];
            int shift = k % M; // 한 바퀴 넘어가면 의미 없으므로 나머지 연산

            for (int j = 0; j < M; j++) {
                if (d == 0) {
                    // 시계 방향: 오른쪽으로 shift
                    // (현재위치 + 이동거리) % M 위치로 이동
                    temp[(j + shift) % M] = map[i][j];
                } else {
                    // 반시계 방향: 왼쪽으로 shift
                    // 자바에서 음수 나머지 처리를 위해 + M 사용
                    temp[(j - shift + M) % M] = map[i][j];
                }
            }
            map[i] = temp;
        }
    }

    // 인접한 수 제거 메서드
    static boolean removeAdjacent() {
        boolean[][] toRemove = new boolean[N + 1][M];
        boolean isRemoved = false; // 하나라도 지워졌는지 확인하는 플래그

        for (int i = 1; i <= N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0) continue; // 이미 지워진 칸은 패스

                int currentVal = map[i][j];

                // 1. 가로 인접 확인 (같은 원판 내 좌우)
                // 오른쪽 확인 (원형 큐처럼 모듈러 연산)
                int nextIdx = (j + 1) % M;
                if (map[i][nextIdx] == currentVal) {
                    toRemove[i][j] = true;
                    toRemove[i][nextIdx] = true;
                    isRemoved = true;
                }

                // 2. 세로 인접 확인 (다른 원판 간 상하)
                // 아래쪽 원판 확인 (마지막 원판 제외)
                if (i < N) {
                    if (map[i + 1][j] == currentVal) {
                        toRemove[i][j] = true;
                        toRemove[i + 1][j] = true;
                        isRemoved = true;
                    }
                }
            }
        }

        // 마킹된 위치의 숫자를 0으로 변경
        if (isRemoved) {
            for (int i = 1; i <= N; i++) {
                for (int j = 0; j < M; j++) {
                    if (toRemove[i][j]) {
                        map[i][j] = 0;
                    }
                }
            }
        }

        return isRemoved;
    }

    // 평균을 구하고 값을 조정하는 메서드
    static void adjustByAverage() {
        double sum = 0;
        int count = 0;

        for (int i = 1; i <= N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] != 0) {
                    sum += map[i][j];
                    count++;
                }
            }
        }

        if (count == 0) return; // 남은 수가 없으면 리턴

        double avg = sum / count;

        for (int i = 1; i <= N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] != 0) {
                    if (map[i][j] > avg) {
                        map[i][j]--;
                    } else if (map[i][j] < avg) {
                        map[i][j]++;
                    }
                    // 같으면 아무것도 안함
                }
            }
        }
    }

    // 최종 합계 계산
    static int calculateSum() {
        int sum = 0;
        for (int i = 1; i <= N; i++) {
            for (int j = 0; j < M; j++) {
                sum += map[i][j];
            }
        }
        return sum;
    }
}
