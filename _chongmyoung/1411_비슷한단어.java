import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();       
        String[] words = new String[N];

        for (int i = 0; i < N; i++) {
            words[i] = sc.next();
        }

        int count = 0;

        // 모든 쌍 비교
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (isSimilar(words[i], words[j])) {
                    count++;
                }
            }
        }

        System.out.println(count);
    }

    static boolean isSimilar(String a, String b) {
        if (a.length() != b.length()) return false;

        Map<Character, Character> mapAB = new HashMap<>();
        Map<Character, Character> mapBA = new HashMap<>();

        for (int i = 0; i < a.length(); i++) {
            char ca = a.charAt(i);
            char cb = b.charAt(i);

            // a -> b 매핑 확인
            if (mapAB.containsKey(ca)) {
                if (mapAB.get(ca) != cb) return false; // 기존 매핑과 충돌
            } else {
                mapAB.put(ca, cb);
            }

            // b -> a 매핑 확인 (역방향)
            if (mapBA.containsKey(cb)) {
                if (mapBA.get(cb) != ca) return false; // 기존 매핑과 충돌
            } else {
                mapBA.put(cb, ca);
            }
        }

        return true;
    }
}
