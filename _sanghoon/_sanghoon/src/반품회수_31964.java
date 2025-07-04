import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 반품회수_31964 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] positions = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] times = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int current = 0;
        int  answer = 0;
        for (int i = N - 1; i >= 0; i--) {
            int distance = Math.abs(positions[i] - current);
            if (times[i] <= answer + distance || times[i] <= distance) {
                answer += distance;
            } else {
                answer += times[i] - answer;
            }
            current = positions[i];
        }
        answer += current;
        System.out.println(answer);
    }
}
