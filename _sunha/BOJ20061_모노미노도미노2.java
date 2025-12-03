/** BOJ20061_모노미노도미노2
 * # 문제
 * - 게임 규칙
 *  1 빨간 보드에 블록을 두면 회대한 오른쪽(파랑)으로 이동한 한개, 또 최대한 아래쪽(초록)으로 이동한 한개, 총 2개가 생김
 *  2 초혹색의 한 행/파란색의 한 열이 가득 찰 경우 그 행/열을 지우고 남은 블록들을 아래/오른쪽으로 이동
 *  3 연한 초록/파랑에 블록이 있는 경우 블록이 있는 행/열의 개수만큼 가장 아래/오른쪽 행/열이 사라짐.
 *  - 우선순위는 2 -> 3이다.
 *
 * - 입력: N/t x y
 *  - t = 1 -> 1*1
 *  - t = 2 -> 1*2
 *  - t = 3 -> 2*1
 *  - 빨간 칸을 침범하는 경우는 없음
 *
 * - 목표: 주어진 대로 게임을 했을 때, 점수와 초록/파랑에 타일이 남아있는 칸의 개수.
 *
 * # 제한
 * - 1초
 *  - 배열로 하면 매번 24+24 번 탐색 해야함... 최대 240,000이라 나쁘지 않은데
 *  - 비트마스킹으로 하면 더 빠를듯?
 * - 512MB
 *
 * # 풀이
 * - 시뮬레이션처럼 해야할 것같은데.
 * - 비트마스킹으로
 * - 너무 일이 많아서 함수로 뺄 수 있는 건 빼고 싶은데.
 */


//import java.io.*;
//public class BOJ20061_모노미노도미노2 {
//    static int score = 0;
//    public static void main(String[] args) throws IOException {
//        // score 선언
//        int N, t, x, y;
//
//        // 파란보드/초록 보드 만들기 -> 비트마스킹 배열로(int[])
//        int[] blue = new int[6];
//        int[] green = new int[6];
//
//        // 입력 받기(N)
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        N = Integer.parseInt(br.readLine());
//
//        // 위치 입력 받으면서 시뮬레이션 돌리기
//        int tile=0, depth, length=0;
//        for (int n=0; n<N; n++) {
//            // x,y,t를 받아서
//            String[] temp = br.readLine().split(" ");
//            t = Integer.parseInt(temp[0]);
//            x = Integer.parseInt(temp[1]);
//            y = Integer.parseInt(temp[2]);
//
//            // 초록보드
//            if (t == 1) {
//                tile = (1<<y);
//                length = 1;
//            }
//            if (t == 2) {
//                tile = (3<<y);
//                length = 1;
//            }
//            if (t == 3) {
//                tile = (1<<y);
//                length = 2;
//            }
//
//            // 각각에 대해서 배열을 0부터 돌면서 막힌 구간을 찾아야해.
//            // 막힌 구간을 찾았으면 그 위로 쌓으면 됨.
//            depth = findDepth(green, tile);
//            green[depth] = green[depth] | tile;
//
//            if (length == 2) {
//                green[depth-1] = green[depth-1] | tile;
//            }
//
//            // 쌓았는데 해당 열(행)이 가득 참
//            // score++
//            // 왼쪽거 한칸씩 이동하면서 덮어쓰기
//
//            if (length == 2) {
//                if (checkFill(green, depth-1)) {
//                    removeLine(green, depth-1);
//                }
//            }
//
//            if (checkFill(green, depth)) {
//                removeLine(green, depth);
//            }
//
//            // 연한 칸(0,1)에 블록이 있음
//            // 1개인지 2개인지 확인하고
//            // 그만큼 덮어쓰기.
//            if (green[0] != 0 && green[1] != 0) {
//                removeLine(green, 5);
//                removeLine(green, 5);
//            }
//            if (green[0] != 0 || green[1] != 0) {
//                removeLine(green, 5);
//            }
//
//            // 파란보드
//            if (t == 1) {
//                tile = (1<<x);
//                length = 1;
//            }
//            if (t == 2) {
//                tile = (1<<x);
//                length = 2;
//            }
//            if (t == 3) {
//                tile = (3<<x);
//                length = 1;
//            }
//
//            // 각각에 대해서 배열을 0부터 돌면서 막힌 구간을 찾아야해.
//            // 막힌 구간을 찾았으면 그 위로 쌓으면 됨.
//            depth = findDepth(blue, tile);
//            blue[depth] = blue[depth] | tile;
//
//            if (length == 2) {
//                blue[depth-1] = blue[depth-1] | tile;
//            }
//
//            // 쌓았는데 해당 열(행)이 가득 참
//            // score++
//            // 왼쪽거 한칸씩 이동하면서 덮어쓰기
//            // 무조건 깊이 작은 거부터 해야됨. -> 아니면 깊은 깊이의 것을 지웠는지 안지웠는지에 따라서 또 분기 해야함.
//            if (length == 2) {
//                if (checkFill(blue, depth-1)) {
//                    removeLine(blue, depth-1);
//                }
//            }
//
//            if (checkFill(blue, depth)) {
//                removeLine(blue, depth);
//            }
//
//            // 연한 칸(0,1)에 블록이 있음
//            // 1개인지 2개인지 확인하고
//            // 그만큼 덮어쓰기.
//            if (blue[0] != 0 && blue[1] != 0) {
//                removeLine(blue, 5);
//                removeLine(blue, 5);
//            }
//            if (blue[0] != 0 || blue[1] != 0) {
//                removeLine(blue, 5);
//            }
//        }
//        int cnt = 0;
//        for (int i=0; i<6; i++) {
//            cnt+= Integer.bitCount(blue[i]);
//            cnt+= Integer.bitCount(green[i]);
//        }
//
//        System.out.println(score);
//        System.out.println(cnt);
//    }
//
//    static int findDepth(int[] board, int pos){
//        for (int i=0; i<board.length; i++) {
//            if ((board[i] & pos) != 0) // 놓을 수 없음
//                return i-1;
//        }
//        return 5;
//    }
//
//    static void removeLine(int[] board, int depth) {
//        for (int i=depth; i>0; i--) {
//            board[i] = board[i-1];
//        }
//        board[0] = 0;
//    }
//
//    static boolean checkFill(int[] board, int depth) {
//        if (board[depth] == 0b1111) {
//            score++;
//            return true;
//        }
//        return false;
//    }
// }

import java.io.*;
public class BOJ20061_모노미노도미노2 {
    static int score = 0;
    public static void main(String[] args) throws IOException {
        // 변수 선언
        int N, t, x, y;

        // 파란보드/초록 보드 만들기 -> 비트마스킹 배열로(int[])
        int[] blue = new int[6];
        int[] green = new int[6];

        // 입력 받기(N)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        // 위치 입력 받으면서 시뮬레이션 돌리기
        int tile=0, depth, length=0;
        for (int n=0; n<N; n++) {
            // x,y,t를 받아서
            String[] temp = br.readLine().split(" ");
            t = Integer.parseInt(temp[0]);
            x = Integer.parseInt(temp[1]);
            y = Integer.parseInt(temp[2]);

            simulation(green, t, y);

            // 파란보드
            if (t == 2) t = 3;
            else if (t == 3) t = 2;

            simulation(blue, t, x);

        }

        int cnt = 0;
        for (int i=0; i<6; i++) {
            cnt+= Integer.bitCount(blue[i]);
            cnt+= Integer.bitCount(green[i]);
        }

        System.out.println(score);
        System.out.println(cnt);
    }

    static void simulation(int[] board, int type, int i) {
        int tile=0, length=0;
        if (type == 1) {
            tile = (1<<i);
            length = 1;
        }
        if (type == 2) {
            tile = (3<<i);
            length = 1;
        }
        if (type == 3) {
            tile = (1<<i);
            length = 2;
        }

        // 각각에 대해서 배열을 0부터 돌면서 막힌 구간을 찾아야해.
        // 막힌 구간을 찾았으면 그 위로 쌓으면 됨.
        int depth = findDepth(board, tile);
        board[depth] = board[depth] | tile;

        if (length == 2)
            board[depth-1] = board[depth-1] | tile;

        // 쌓았는데 해당 열(행)이 가득 참
        // score++
        // 왼쪽거 한칸씩 이동하면서 덮어쓰기
        if (length == 2) {
            if (checkFill(board, depth-1))
                removeLine(board, depth-1);
        }

        if (checkFill(board, depth))
            removeLine(board, depth);

        // 연한 칸(0,1)에 블록이 있음
        // 1개인지 2개인지 확인하고
        // 그만큼 덮어쓰기.
        int light = 0;
        if (board[0] != 0) light++;
        if (board[1] != 0) light++;

        while (light-- > 0) {
            removeLine(board, 5);
        }
    }

    static int findDepth(int[] board, int pos){
        for (int i=0; i<board.length; i++) {
            if ((board[i] & pos) != 0) // 놓을 수 없음
                return i-1;
        }
        return 5;
    }

    static void removeLine(int[] board, int depth) {
        for (int i=depth; i>0; i--) {
            board[i] = board[i-1];
        }
        board[0] = 0;
    }

    static boolean checkFill(int[] board, int depth) {
        if (board[depth] == 0b1111) {
            score++;
            return true;
        }
        return false;
    }
}
