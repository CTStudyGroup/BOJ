import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine().trim());
        double A = Double.parseDouble(st.nextToken());
        double B = Double.parseDouble(st.nextToken());
        double C = Double.parseDouble(st.nextToken());

        // 탐색 구간
        double lo = Math.max(0.0, (C - B) / A);
        double hi = (C + B) / A;

        // 이분탐색
        for (int it = 0; it < 200; it++) { // 200번이면 2^-200 수준으로 충분히 정확
            double mid = (lo + hi) / 2.0;
            double f = A * mid + B * Math.sin(mid) - C;
            if (f < 0) lo = mid;
            else hi = mid;
        }

        System.out.println(String.format(Locale.US, "%.15f", (lo + hi) / 2.0));
    }
}
