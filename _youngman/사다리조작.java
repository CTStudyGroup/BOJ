import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();
        int answer = 0;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            st.nextToken();                 // x좌표는 필요 없음
            int y = Integer.parseInt(st.nextToken());

            // y보다 높은 건물들은 이제 끝났다고 판단 → pop
            while (!stack.isEmpty() && stack.peek() > y) {
                stack.pop();
                answer++;
            }

            // 같은 높이는 중복해서 넣을 필요 없음
            if (!stack.isEmpty() && stack.peek() == y) continue;

            // y가 0이 아니면 push (높이가 0이면 건물 없음)
            if (y > 0) stack.push(y);
        }

        // 스택에 남아있는 높이들 처리
        while (!stack.isEmpty()) {
            stack.pop();
            answer++;
        }

        System.out.println(answer);
    }
}
