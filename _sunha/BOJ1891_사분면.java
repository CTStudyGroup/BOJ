import java.io.*;

/** BOJ1891_사분면
 * # 문제
 * 사분면을 계속 쪼개면서 번호를 붙임 -> 1 / 11 / 111 같이
 * 이때 쪼개진 사분면을 이동할 때 도착한 사분면의 번호를 구해야함. || -1
 *
 * # 제한
 * - 시간: 2초
 * - 공간: 128MB
 * - 입력
 *  - 1 ≤ 사분면 번호의 자릿수 ≤ 50 -> 사분면 번호 String.. or BigInteger
 *  - |x|, |y| ≤ 2^50 -> long
 *
 * # 풀이
 *  - 분할 정복으로 풀면될것같은데
 *  - 엥 아니 그냥 계산만 해도 될듯?
 *  - ~~ 라고 쉽게 생각했는데 아니었다.
 *  - 이동이랑 위치 찾기를 동시에 생각하니까 완전 꼬임
 *  - 그게 아니라 배열 좌표로 쉽게 이동하고 변환을 분할정복으로...
 *
 */

public class BOJ1891_사분면 {
    static int N;
    static long X, Y, r, c;
    static String start;

    public static void main(String[] args) throws IOException {
        // 입력 받고
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        start = temp[1];

        temp = br.readLine().split(" ");
        X = Long.parseLong(temp[0]);
        Y = Long.parseLong(temp[1]);

        long size = 1L << N;

        // 배열 좌표로 변환
        convertToPos(0,  0L, 0L, size);

        // 이동
        r += X;
        c -= Y;

        if (r < 0 || r >= size || c < 0 || c >= size) {
            System.out.println(-1);
            return;
        }

        // 좌표를 번호로 변환
        System.out.println(convertToNum(r,c, size));


    }

    static String convertToNum(long r, long c, long size) {
        if (size == 1) return "";

        long newSize = size/2;

        if (r < newSize && c < newSize) {
            return "2" + convertToNum(r, c, newSize);
        }
        else if (r >= newSize && c < newSize) {
            return "1" + convertToNum(r - newSize, c, newSize);
        }
        else if (r < newSize && c >= newSize) {
            return "3" + convertToNum(r, c - newSize, newSize);
        }
        else {
            return "4" + convertToNum(r - newSize, c - newSize, newSize);
        }

    }


    static void convertToPos(int depth, long sr, long sc, long size) {
        if (depth == N && size == 1) {
            r = sr;
            c = sc;
            return;
        }

        switch (start.charAt(depth)) {
            case '2':
                convertToPos(depth+1, sr, sc, size/2);
                break;
            case '1':
                convertToPos(depth+1, sr + size/2, sc, size/2);
                break;
            case '3':
                convertToPos(depth+1, sr, sc + size/2, size/2);
                break;
            case '4':
                convertToPos(depth+1, sr + size/2, sc + size/2, size/2);
                break;
        }
    }


}
