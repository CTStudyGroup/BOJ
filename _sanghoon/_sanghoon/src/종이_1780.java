import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 종이_1780 {
    static int[][] arr;
    static int minus;
    static int one;
    static int zero;
    public static void main(String[] args) throws IOException {

        // N * M 크기의 행렬
        // 종이의 각 칸은 -1, 0, 1
        // 종이가 모두 같은 수로 -> 그ㄷ로 사용
        // 아닌 경우 종이를 같은 크기의 종이 9개로 자름
        // -1, 0, 1로만 채워진 종이의 개수 구하기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            arr[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        recur(0, N, 0, N);

        System.out.println(minus);
        System.out.println(zero);
        System.out.println(one);

    }

    static void recur(int rStart, int rEnd, int cStart,  int cEnd) {
        if (check(rStart, rEnd, cStart, cEnd)) {
            if (arr[rStart][cStart] == -1) {
                minus++;
            } else if (arr[rStart][cStart] == 0) {
                zero++;
            } else {
                one++;
            }
            return;
        }

        int rFirstMid = rStart + ((rEnd - rStart) / 3);
        int cFirstMid = cStart + ((cEnd - cStart) / 3);
        int rSecMid = rStart + 2 * ((rEnd - rStart) / 3);
        int cSecMid = cStart + 2 * ((cEnd - cStart) / 3);

        recur(rStart, rFirstMid, cStart, cFirstMid);
        recur(rStart, rFirstMid, cFirstMid, cSecMid);
        recur(rStart, rFirstMid, cSecMid, cEnd);

        recur(rFirstMid, rSecMid, cStart, cFirstMid);
        recur(rFirstMid, rSecMid, cFirstMid, cSecMid);
        recur(rFirstMid, rSecMid, cSecMid, cEnd);

        recur(rSecMid, rEnd, cStart, cFirstMid);
        recur(rSecMid, rEnd, cFirstMid, cSecMid);
        recur(rSecMid, rEnd, cSecMid, cEnd);

    }

    static boolean check(int rStart, int rEnd, int cStart, int cEnd) {
        int firstValue = arr[rStart][cStart];
        for (int r = rStart; r < rEnd; r++) {
            for (int c = cStart; c < cEnd; c++) {
                if (arr[r][c] != firstValue) {
                    return false;
                }
            }
        }
        return true;
    }
}
