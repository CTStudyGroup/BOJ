import java.io.*;
import java.util.*;

public class Main {
    static String s;
    static ArrayList<int[]> pairs = new ArrayList<>();
    static boolean[] remove;
    static HashSet<String> result = new HashSet<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = br.readLine();

        // 1. 괄호 쌍 찾기
        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') st.push(i);
            else if (s.charAt(i) == ')') {
                int open = st.pop();
                pairs.add(new int[]{open, i});
            }
        }

        remove = new boolean[s.length()];

        // 2. 모든 괄호쌍 선택 조합(부분집합)
        subset(0);

        ArrayList<String> list = new ArrayList<>(result);
        Collections.sort(list);
        for (String str : list) System.out.println(str);
    }

    // 부분집합으로 괄호쌍 선택
    static void subset(int idx) {
        if (idx == pairs.size()) {
            build();
            return;
        }

        // 괄호쌍을 제거하지 않는 경우
        subset(idx + 1);

        // 괄호쌍을 제거하는 경우
        int[] p = pairs.get(idx);
        remove[p[0]] = true;
        remove[p[1]] = true;

        subset(idx + 1);

        // 원상복구
        remove[p[0]] = false;
        remove[p[1]] = false;
    }

    // 문자열 구성 후 삽입
    static void build() {
        StringBuilder sb = new StringBuilder();
        boolean removed = false;

        for (int i = 0; i < s.length(); i++) {
            if (!remove[i]) sb.append(s.charAt(i));
            else removed = true;
        }

        // 최소 하나는 제거해야 함
        if (removed) result.add(sb.toString());
    }
}
