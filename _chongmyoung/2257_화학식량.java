import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().trim();

        Deque<Integer> st = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch == '(') {
                st.push(-1); // 구분자
            } else if (ch == ')') {
                int sum = 0;
                while (!st.isEmpty() && st.peek() != -1) sum += st.pop();
                st.pop(); // '(' 제거
                st.push(sum); // 괄호 그룹 합
            } else if (ch == 'H' || ch == 'C' || ch == 'O') {
                int val = (ch == 'H') ? 1 : (ch == 'C') ? 12 : 16;
                st.push(val);
            } else { // 숫자 2~9
                int mul = ch - '0';
                int top = st.pop();
                st.push(top * mul);
            }
        }

        int ans = 0;
        while (!st.isEmpty()) ans += st.pop();
        System.out.println(ans);
    }
}
