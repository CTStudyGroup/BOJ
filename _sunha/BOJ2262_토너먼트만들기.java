import java.util.*;

public class BOJ2262_토너먼트만들기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            list.add(sc.nextInt());
        }

        int totalDiff = 0;

        while (list.size() > 1) {
            int maxIdx = 0;
            int maxVal = list.get(0);

            for (int i = 1; i < list.size(); i++) {
                if (list.get(i) > maxVal) {
                    maxVal = list.get(i);
                    maxIdx = i;
                }
            }

            int diff = Integer.MAX_VALUE;

            if (maxIdx > 0) {
                diff = Math.min(diff, maxVal - list.get(maxIdx - 1));
            }

            if (maxIdx < list.size() - 1) {
                diff = Math.min(diff, maxVal - list.get(maxIdx + 1));
            }

            totalDiff += diff;
            list.remove(maxIdx);
        }

        System.out.println(totalDiff);
    }
}