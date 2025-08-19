import java.util.*;

public class Main {
    static String A, B, C;
    static int[][] visited; // -1: 미방문, 0: 실패, 1: 성공
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); // 테스트 케이스 개수
        
        for (int t = 1; t <= T; t++) {
            A = sc.next();
            B = sc.next();
            C = sc.next();
            
            visited = new int[A.length() + 1][B.length() + 1];
            for (int[] row : visited) Arrays.fill(row, -1);
            
            boolean possible = dfs(0, 0, 0);
            
            System.out.printf("Data set %d: %s\n", t, (possible ? "yes" : "no"));
        }
    }
    
    static boolean dfs(int i, int j, int k) {
        if (k == C.length()) return (i == A.length() && j == B.length());
        if (visited[i][j] != -1) return visited[i][j] == 1;
        
        boolean ok = false;
        
        // A에서 문자 사용 가능할 때
        if (i < A.length() && A.charAt(i) == C.charAt(k)) {
            ok |= dfs(i + 1, j, k + 1);
        }
        
        // B에서 문자 사용 가능할 때
        if (j < B.length() && B.charAt(j) == C.charAt(k)) {
            ok |= dfs(i, j + 1, k + 1);
        }
        
        visited[i][j] = ok ? 1 : 0;
        return ok;
    }
}
