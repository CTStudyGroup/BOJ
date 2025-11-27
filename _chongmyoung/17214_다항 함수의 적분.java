import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().trim();
        if (s.equals("0")) { // 특수 케이스: 0이면 상수항만 존재 -> W
            System.out.println("W");
            return;
        }

        int xIdx = s.indexOf('x');
        StringBuilder sb = new StringBuilder();

        if (xIdx == -1) {
            // 상수항만 있음: k -> kx + W
            int k = Integer.parseInt(s);
            if (k == 1) sb.append("x+W");
            else if (k == -1) sb.append("-x+W");
            else sb.append(k).append("x+W");
            System.out.println(sb.toString());
            return;
        }

        // x가 있는 경우 (일차항 존재)
        String coefStr = s.substring(0, xIdx);
        int coef;
        if (coefStr.equals("") || coefStr.equals("+")) coef = 1;
        else if (coefStr.equals("-")) coef = -1;
        else coef = Integer.parseInt(coefStr);

        // 적분 후 이차항의 계수
        int a = coef / 2;

        // x 뒤의 부분(상수항). 존재하지 않으면 0
        String tail = s.substring(xIdx + 1);
        int b = 0;
        if (!tail.equals("")) b = Integer.parseInt(tail);

        // 이차항 출력
        if (a == 1) sb.append("xx");
        else if (a == -1) sb.append("-xx");
        else sb.append(a).append("xx");

        // 일차항 출력 (b가 0이면 생략)
        if (b != 0) {
            if (b > 0) sb.append("+");
            // b의 절댓값이 1이면 숫자 1 생략
            if (b == 1) sb.append("x");
            else if (b == -1) sb.append("-x");
            else sb.append(b).append("x");
            sb.append("+W");
        } else {
            // 상수항(원래 상수 없음)인 경우 "+W" 추가
            sb.append("+W");
        }

        System.out.println(sb.toString());
    }
}
