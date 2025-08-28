import java.io.*;
import java.util.*;

public class Main {
    static int N, L, R, X;
    static int[] arr;
    static int answer = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        L = sc.nextInt();
        R = sc.nextInt();
        X = sc.nextInt();
        arr = new int[N];
        
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        dfs(0, Integer.MAX_VALUE, Integer.MIN_VALUE, 0, 0);
        System.out.println(answer);
    }

    static void dfs(int idx, int min, int max, int sum, int count) {
        if(idx == N){
            if(count >= 2 && sum >= L && sum <= R &&  (max - min) >= X){
                answer++;
            }
            return;
        }
        dfs(idx+1, Math.min(min, arr[idx]), Math.max(max, arr[idx]), sum+arr[idx], count+1);
        dfs(idx+1, min, max, sum, count);
    }
}
