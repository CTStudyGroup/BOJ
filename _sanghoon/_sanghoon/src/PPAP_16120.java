import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;

public class PPAP_16120 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split("");

        List<String> stack = new LinkedList<>();

        for (String s : input) {
            stack.add(s);
            if (stack.size() >= 4 && stack.get(stack.size() - 1).equals("P")) {
                if ("PPAP".equals(String.join("", stack.subList(stack.size() - 4, stack.size())))) {
                    stack.remove(stack.size() - 1);
                    stack.remove(stack.size() - 1);
                    stack.remove(stack.size() - 1);
                }
            }
        }

        if (stack.size() == 1 && stack.get(stack.size() - 1).equals("P")) {
            System.out.print("PPAP");
        } else {
            System.out.print("NP");
        }

    }
}
