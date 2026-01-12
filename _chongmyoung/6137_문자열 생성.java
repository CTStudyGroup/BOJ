import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 1. 입력 받기
        int N = Integer.parseInt(br.readLine());
        char[] arr = new char[N];
        
        for (int i = 0; i < N; i++) {
            // 입력이 한 줄에 한 글자씩 들어옴 (공백 제거 필요할 수 있으므로 trim 사용 권장)
            String line = br.readLine();
            arr[i] = line.charAt(0);
        }
        
        StringBuilder sb = new StringBuilder();
        int left = 0;
        int right = N - 1;
        int count = 0; // 출력 줄바꿈용 카운터
        
        // 2. 투 포인터로 문자열 생성
        while (left <= right) {
            // 왼쪽 문자가 더 작으면 왼쪽 선택
            if (arr[left] < arr[right]) {
                sb.append(arr[left++]);
            } 
            // 오른쪽 문자가 더 작으면 오른쪽 선택
            else if (arr[left] > arr[right]) {
                sb.append(arr[right--]);
            } 
            // 두 문자가 같으면 안쪽을 확인해야 함
            else {
                int l = left + 1;
                int r = right - 1;
                boolean isLeftSmaller = true; // 기본값: 같으면 왼쪽 먼저라고 가정(어차피 대칭이면 상관없음)
                
                while (l <= r) {
                    if (arr[l] < arr[r]) {
                        isLeftSmaller = true;
                        break;
                    } else if (arr[l] > arr[r]) {
                        isLeftSmaller = false;
                        break;
                    }
                    l++;
                    r--;
                }
                
                if (isLeftSmaller) {
                    sb.append(arr[left++]);
                } else {
                    sb.append(arr[right--]);
                }
            }
            
            // 3. 80글자마다 줄바꿈 처리
            count++;
            if (count % 80 == 0) {
                sb.append('\n');
            }
        }
        
        // 결과 출력
        System.out.println(sb.toString());
    }
}
