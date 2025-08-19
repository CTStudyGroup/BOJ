import java.util.*;

public class Main {
    static int N;                 // 숫자의 개수
    static int[] numbers;         // 숫자 배열
    static int[] operators = new int[4]; // +, -, *, / 연산자의 개수
    static int max = Integer.MIN_VALUE; // 최댓값 저장
    static int min = Integer.MAX_VALUE; // 최솟값 저장

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = sc.nextInt();
        }
        for (int i = 0; i < 4; i++) {
            operators[i] = sc.nextInt(); // + - * / 개수 입력
        }

        dfs(1, numbers[0]); // 첫 번째 숫자부터 시작
        System.out.println(max);
        System.out.println(min);
    }

    // DFS로 연산자 배치 탐색
    static void dfs(int depth, int result) {
        // 모든 숫자를 다 사용한 경우
        if (depth == N) {
            max = Math.max(max, result);
            min = Math.min(min, result);
            return;
        }

        // 각 연산자 종류별로 탐색
        for (int i = 0; i < 4; i++) {
            if (operators[i] > 0) { // 남은 연산자가 있을 경우
                operators[i]--;     // 해당 연산자 사용

                switch (i) {
                    case 0: // +
                        dfs(depth + 1, result + numbers[depth]);
                        break;
                    case 1: // -
                        dfs(depth + 1, result - numbers[depth]);
                        break;
                    case 2: // *
                        dfs(depth + 1, result * numbers[depth]);
                        break;
                    case 3: // /
                        dfs(depth + 1, result / numbers[depth]);
                        break;
                }

                operators[i]++; // 백트래킹
            }
        }
    }
}
