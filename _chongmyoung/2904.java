import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입출력을 위해 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // 1. 전체 숫자들의 소인수 총합을 저장할 맵 (소수 -> 총 개수)
        Map<Integer, Integer> totalMap = new HashMap<>();
        
        // 2. 각 숫자별 소인수 개수를 저장할 리스트 (각 인덱스가 숫자에 해당, 값은 맵)
        List<Map<Integer, Integer>> individualMaps = new ArrayList<>();
        
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            Map<Integer, Integer> currentMap = new HashMap<>();
            
            // 소인수분해 수행
            // 2부터 루트 num까지 나눠보며 소인수 찾기
            for (int j = 2; j * j <= num; j++) {
                while (num % j == 0) {
                    // 전체 카운트 증가
                    totalMap.put(j, totalMap.getOrDefault(j, 0) + 1);
                    // 현재 숫자의 카운트 증가
                    currentMap.put(j, currentMap.getOrDefault(j, 0) + 1);
                    num /= j;
                }
            }
            // 나누고 남은 수가 1보다 크면 그 자체도 소수임
            if (num > 1) {
                totalMap.put(num, totalMap.getOrDefault(num, 0) + 1);
                currentMap.put(num, currentMap.getOrDefault(num, 0) + 1);
            }
            
            individualMaps.add(currentMap);
        }
        
        long gcd = 1; // 최대공약수 점수
        int moves = 0; // 최소 이동 횟수
        
        // 발견된 모든 소수에 대해 계산
        for (Integer prime : totalMap.keySet()) {
            int totalCount = totalMap.get(prime);
            int targetCount = totalCount / N; // N개의 숫자가 공평하게 가져야 할 목표 개수
            
            // 목표 개수가 0이면 건너뜀 (모든 수에 분배 불가능)
            if (targetCount == 0) continue;
            
            // 1. 최대공약수(점수) 계산: 소수^목표개수 만큼 곱하기
            for (int k = 0; k < targetCount; k++) {
                gcd *= prime;
            }
            
            // 2. 이동 횟수 계산
            for (int i = 0; i < N; i++) {
                // i번째 숫자가 현재 가지고 있는 prime의 개수
                int currentHas = individualMaps.get(i).getOrDefault(prime, 0);
                
                // 목표보다 적게 가지고 있다면, 부족한 만큼 채워야 함 (이동 발생)
                if (currentHas < targetCount) {
                    moves += (targetCount - currentHas);
                }
            }
        }
        
        System.out.println(gcd + " " + moves);
    }
}
