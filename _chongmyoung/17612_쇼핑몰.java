import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    /**
     * 고객 입장 규칙을 위한 계산대(Counter) 정보 클래스
     * 1. 계산 종료 시간이 빠른 순 (오름차순)
     * 2. 계산대 번호가 작은 순 (오름차순)
     */
    static class Counter {
        int id;      // 계산대 번호 (1부터 K까지)
        long endTime; // 현재 계산대에서 계산이 끝나는 시간

        public Counter(int id, long endTime) {
            this.id = id;
            this.endTime = endTime;
        }

        // 고객 입장 Comparator
        public static Comparator<Counter> EntranceComparator = (c1, c2) -> {
            // 1. 계산 종료 시간이 다르면, 빠른 시간(작은 값)이 우선
            if (c1.endTime != c2.endTime) {
                return Long.compare(c1.endTime, c2.endTime);
            }
            // 2. 종료 시간이 같으면, 계산대 번호가 작은 곳(작은 값)이 우선
            return Integer.compare(c1.id, c2.id);
        };
    }

    /**
     * 고객 퇴장 규칙을 위한 고객(Customer) 정보 클래스
     * 1. 퇴장 시간이 빠른 순 (오름차순)
     * 2. 계산대 번호가 높은 순 (내림차순)
     */
    static class Customer {
        int id;         // 고객 ID (회원 번호)
        int counterId;  // 배정받았던 계산대 번호
        long exitTime;  // 고객이 퇴장하는 시간

        public Customer(int id, int counterId, long exitTime) {
            this.id = id;
            this.counterId = counterId;
            this.exitTime = exitTime;
        }

        // 고객 퇴장 Comparator
        public static Comparator<Customer> ExitComparator = (c1, c2) -> {
            // 1. 퇴장 시간이 다르면, 빠른 시간(작은 값)이 우선
            if (c1.exitTime != c2.exitTime) {
                return Long.compare(c1.exitTime, c2.exitTime);
            }
            // 2. 퇴장 시간이 같으면, 계산대 번호가 큰 곳(큰 값)이 우선 (내림차순)
            return Integer.compare(c2.counterId, c1.counterId);
        };
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 고객 수
        int K = Integer.parseInt(st.nextToken()); // 계산대 수

        // 1. 고객 입장 처리를 위한 우선순위 큐 (계산대 상태 관리)
        PriorityQueue<Counter> pq_counter = new PriorityQueue<>(Counter.EntranceComparator);
        
        // 2. 고객 퇴장 처리를 위한 우선순위 큐 (퇴장 순서 결정)
        PriorityQueue<Customer> pq_exit = new PriorityQueue<>(Customer.ExitComparator);

        // --- 초기화: K개의 계산대를 pq_counter에 추가 ---
        // 모든 계산대의 초기 종료 시간은 0
        for (int i = 1; i <= K; i++) {
            pq_counter.add(new Counter(i, 0));
        }

        // --- 시뮬레이션: N명의 고객 처리 ---
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int customerId = Integer.parseInt(st.nextToken());
            int processingTime = Integer.parseInt(st.nextToken()); // 물건 개수 W

            // 1. 가장 빨리 끝나는 계산대 선택 (pq_counter에서 poll)
            Counter assignedCounter = pq_counter.poll();
            
            // 2. 새로운 계산 종료 시간 계산
            long newExitTime = assignedCounter.endTime + processingTime;
            
            // 3. 고객 정보를 pq_exit에 추가 (퇴장 순서 결정을 위해)
            pq_exit.add(new Customer(customerId, assignedCounter.id, newExitTime));
            
            // 4. 계산대 정보를 업데이트하고 pq_counter에 다시 추가 (다음 고객을 받을 준비)
            assignedCounter.endTime = newExitTime;
            pq_counter.add(assignedCounter);
        }

        // --- 결과 계산: 고객 퇴장 순서대로 가중치 합산 ---
        long totalResult = 0;
        
        // 퇴장 순서 (1부터 N까지)
        for (int i = 1; i <= N; i++) {
            Customer exitedCustomer = pq_exit.poll();
            
            // 총합 = Sigma (고객 ID * 퇴장 순서)
            // 주의: 결과가 매우 커질 수 있으므로 long 타입 사용
            totalResult += (exitedCustomer.id * (long)i);
        }

        System.out.println(totalResult);
    }
}
