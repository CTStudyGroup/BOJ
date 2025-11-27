package 백준;

import java.io.*;
import java.util.*;

public class 사다리조작 {
    static int N, M, H;
    static boolean[][] ladder;
    static int answer = 4;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        ladder = new boolean[H+1][N+1];

        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()); // row
            int b = Integer.parseInt(st.nextToken()); // col
            ladder[a][b] = true;
        }

        dfs(0, 1, 1);

        System.out.println(answer == 4 ? -1 : answer);
    }

    static void dfs(int count, int row, int col){
        if(count >= answer) return;

        if(isCorrect()){
            answer = count;
            return;
        }

        if(count == 3) return;

        for (int i = row; i <= H; i++) {
            int startCol = (i == row ? col : 1);  // 첫 줄만 col부터, 그 다음 줄은 1부터
            for (int j = startCol; j < N; j++) {
                if (ladder[i][j] || ladder[i][j - 1] || ladder[i][j + 1]) continue;

                ladder[i][j] = true;
                dfs(count + 1, i, j + 1);
                ladder[i][j] = false;
            }
        }
    }

    static boolean isCorrect(){
        for(int i=1; i<=N; i++){
            int x = i;
            for(int r=1; r<=H; r++){
                if(ladder[r][x]) x++;
                else if(x>1 && ladder[r][x-1]) x--;
            }
            if(x != i) return false;
        }
        return true;
    }
}
