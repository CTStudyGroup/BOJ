import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static int d;
    public static String num;
    public static Element dxdy, nxny;
    public static String answer = "";

    public static class Element {
        long x, y;
        public Element(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedWriter bw  = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        d = Integer.parseInt(st.nextToken());
        num = st.nextToken();
        st = new StringTokenizer(br.readLine());
        long x = Long.parseLong(st.nextToken());
        long y = Long.parseLong(st.nextToken());
        long n = 1L << d, m = n;


        find(0, n, 0, m, 0);
        nxny = new Element((-1 * y) + dxdy.x, x + dxdy.y);

        if (0 <= nxny.x && nxny.x < n && 0 <= nxny.y && nxny.y < m) {
            check(0, n, 0, m);
            bw.write(answer);
        }
        else bw.write("-1");
        bw.flush();

    }

    private static String check(long n1, long n2, long m1, long m2) {
        if (answer.length() == d) return answer;
        if (n1 <= nxny.x && nxny.x < (n1 + n2) / 2 && (m1 + m2) / 2 <= nxny.y && nxny.y < m2) {
            answer += "1";
            return check(n1, (n1 + n2) / 2, (m1 + m2) / 2, m2);
        } else if (n1 <= nxny.x && nxny.x < (n1 + n2) / 2 && m1 <= nxny.y && nxny.y < (m1 + m2) / 2) {
            answer += "2";
            return check(n1, (n1 + n2) / 2, m1, (m1 + m2) / 2);
        } else if ((n1 + n2) / 2 <= nxny.x && nxny.x < n2 && m1 <= nxny.y && nxny.y < (m1+m2) / 2) {
            answer += "3";
            return check((n1 + n2) / 2, n2, m1, (m1 + m2) / 2);
        } else {
            answer += "4";
            return check((n1 + n2) / 2, n2, (m1 + m2) / 2, m2);
        }
    }

    private static void find(long n1, long n2, long m1, long m2, int index) {
        if (index == d) {
            dxdy = new Element(n1, m1);
            return;
        }
        int number = num.charAt(Integer.parseInt(String.valueOf(index))) - '0';

        if (number == 1) find(n1, (n1 + n2) / 2, (m1 + m2) / 2, m2, index + 1);
        else if (number == 2) find(n1, (n1 + n2) / 2, m1, (m1 + m2) / 2, index + 1);
        else if (number == 3) find((n1 + n2) / 2, n2, m1, (m1 + m2) / 2, index + 1);
        else if (number == 4) find((n1 + n2) / 2, n2, (m1 + m2) / 2, m2, index + 1);
    }


}