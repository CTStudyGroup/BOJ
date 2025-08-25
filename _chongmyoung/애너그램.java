import java.io.*;
import java.util.*;

public class Main {
    static int[] check;
    static StringBuilder sb;
    static Set<String> set;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder result = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        while (n-- > 0) {
            set = new TreeSet<>();
            char[] arr = br.readLine().toCharArray();
            check = new int[26];
            for (char c : arr) {
                check[c - 'a']++;
            }
            sb = new StringBuilder();
            generateAnagrams(arr.length);
            for (String s : set) {
                result.append(s).append("\n");
            }
        }
        System.out.println(result.toString());
    }

    static void generateAnagrams(int r) {
        if (sb.length() == r) {
            set.add(sb.toString());
            return;
        }

        for (int i = 0; i < 26; i++) {
            if (check[i] > 0) {
                check[i]--;
                sb.append((char) (i + 'a'));
                generateAnagrams(r);
                sb.deleteCharAt(sb.length() - 1);
                check[i]++;
            }
        }
    }
}
