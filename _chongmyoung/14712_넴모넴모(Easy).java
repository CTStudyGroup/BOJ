import java.util.*;

public class Main {
    static int[][] board;
    static int N;
    static int M;
    static int answer = 0;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        board = new int[N][M];

        dfs(0, 0);
        System.out.println(answer);
    }

    static void dfs(int r, int c) {
        if(r == N){
            answer++;
            return;
        }

        int nr = r, nc = c + 1;
        if(nc == M){
            nr++;
            nc = 0;
        }

        dfs(nr, nc);

        board[r][c] = 1;
        if(!isBad(r, c)) {
            dfs(nr, nc);
        }
        board[r][c] = 0;
    }

    static boolean isBad(int r, int c) {
        if(r - 1 < 0 || c - 1 < 0) return false;
        return board[r][c] == 1 && board[r - 1][c] == 1
            && board[r][c-1] == 1 && board[r-1][c - 1] == 1;
    }
}
