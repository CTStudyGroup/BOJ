import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class 에디터_1406 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        LinkedList<String> list = Arrays.stream(br.readLine().split("")).collect(Collectors.toCollection(LinkedList::new));

        int M = Integer.parseInt(br.readLine());

        ListIterator<String> iterator = list.listIterator();
        while (iterator.hasNext()) {
            iterator.next();
        }

        for (int i = 0; i < M; i++) {
            String input = br.readLine();
            StringTokenizer st = new StringTokenizer(input);
            String order = st.nextToken();

            switch (order) {
                case "P":
                    String value = st.nextToken();
                    iterator.add(value);
                    break;

                case "L":
                    if (iterator.hasPrevious()) {
                        iterator.previous();
                    }
                    break;

                case "D":
                    if (iterator.hasNext()) {
                        iterator.next();
                    }
                    break;

                case "B":
                    if (iterator.hasPrevious()) {
                        iterator.previous();
                        iterator.remove();
                    }
                    break;

            }
        }

        StringBuilder sb = new StringBuilder();
        for (String s : list) {
            sb.append(s);
        }
        System.out.println(sb);
    }
}
