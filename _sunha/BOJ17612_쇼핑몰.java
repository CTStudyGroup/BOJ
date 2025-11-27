/** BOJ17612_쇼핑몰
 * # 문제
 * - N: 사람 수
 * - w: 사람별 걸리는 시간(산 물건 수)
 * - 입장 -> 작은 수의 계산대 부터, 퇴장 -> 큰 수의 계산대부터
 * - 목표: 쇼핑몰을 나오는 순서를 구하기.
 *
 * #제한
 * - 변수 범위 -> int 가능
 *  - 1 ≤ N ≤ 100,000
 *  - 1 ≤ idi ≤ 1,000,000
 *  - 1 ≤ wi ≤ 20
 *
 * - 시간: 1억번 ->
 *
 *
 * # 풀이
 * - 그냥 우선순위 큐 쓰면 안되나? -> 시간 초과?
 *  - heap -> nlogn -> 20*100,000 -> 2,000,000 가능인데?
 *  - 우선 순위 큐에 2개 쓰자
 *      - 계산중: [계산대, id, w] -> Customer
 *      - 여유: [계산대,  사용시간] -> int
 *  - 입력 받기
 *
 */

//import java.io.*;
//import java.util.*;
//
//// Customer 클래스 선언
//class Customer implements Comparable<Customer>{
//    int id, w;
//    Counter c;
//
//    public Customer(int id, int w) {
//        this.id = id;
//        this.w = w;
//    }
//
//    @Override
//    public int compareTo(Customer o) {
//        if (this.c.end_time == o.c.end_time) {
//            return o.c.id - this.c.id; // 퇴장시에는 큰 수부터
//        }
//        return this.c.end_time - o.c.end_time;
//    }
//}
//
//class Counter implements Comparable<Counter> {
//    int id, end_time = 0;
//
//    public Counter(int id) {
//        this.id = id;
//    }
//
//    @Override
//    public int compareTo(Counter o) {
//        if (this.end_time == o.end_time) {
//            return this.id - o.id; // 입장시에는 작은 수부터
//        }
//        return this.end_time - o.end_time;
//    }
//}
//
//public class Main {
//    public static void main(String[] args) throws IOException {
//        // 기본 입력 받기 / 기본 선언(cnt/result)
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int N, k, cnt=0;
//        long result=0;
//        Customer[] customers;
//
//        String[] temp = br.readLine().split(" ");
//        N = Integer.parseInt(temp[0]);
//        k = Integer.parseInt(temp[1]);
//
//        // N번 돌면서 customer 생성 / customers 배열에 넣어두기
//        customers = new Customer[N+1];
//        for (int n=0; n<N; n++) {
//            temp = br.readLine().split(" ");
//            int id = Integer.parseInt(temp[0]);
//            int w = Integer.parseInt(temp[1]);
//
//            customers[n] = new Customer(id, w);
//        }
//
//        // 우선순위큐 선언
//        // 계산대 (1-k)
//        PriorityQueue<Counter> counters = new PriorityQueue<>();
//        for (int id=1; id<=k; id++) {
//            counters.offer(new Counter(id));
//        }
//        // 계산중 (빈 배열) -> 1번 손님 삽입
//        PriorityQueue<Customer> calculating = new PriorityQueue<>();
//
//
//        // customer 배열 돌면서
//        for (int n=0; n<N; n++) {
//            Customer now = customers[n];
//            // 계산대 비었음
//            if (counters.isEmpty() || (!calculating.isEmpty() && counters.peek().end_time == calculating.peek().c.end_time)) {
//                // 계산중 큐에서 하나 pop
//                Customer out = calculating.poll();
//                System.out.println("out: " + out.id);
//                // 해당 손님id*cnt를 result에 더하고
//                result += (long) out.id * cnt;
//                cnt++;
//                // 해당 계산대는 계산대 큐에 넣기
//                counters.offer(out.c);
//            }
//
//            // 계산대 남았음
//            // 계산대 pop -> 계산대 사용시간 += 현재 손님w
//            Counter counter = counters.poll();
//            System.out.println("counter: " + counter.id);
//            counter.end_time += now.w;
//            // 현재 손님의 계산대를 바꾸고 계산중 큐에 넣음.
//            now.c = counter;
//            calculating.offer(now);
//        }
//
//        while (!calculating.isEmpty()) {
//            Customer out = calculating.poll();
//            result += (long) out.id * cnt;
//            cnt++;
//        }
//
//        System.out.println(result);
//    }
//}
import java.io.*;
import java.util.*;

class Customer implements Comparable<Customer>{
    int id, end_time, counter;

    public Customer(int id, int end_time, int counter) {
        this.id = id;
        this.end_time = end_time;
        this.counter = counter;
    }

    @Override
    public int compareTo(Customer o) {
        if (this.end_time == o.end_time) {
            return o.counter - this.counter; // 퇴장시에는 큰 수부터
        }
        return this.end_time - o.end_time;
    }
}

class Counter implements Comparable<Counter> {
    int id, end_time = 0, user;
//    Customer user;

    public Counter(int id) {
        this.id = id;
    }

    @Override
    public int compareTo(Counter o) {
        if (this.end_time == o.end_time) {
            return this.id - o.id; // 입장시에는 작은 수부터
        }
        return this.end_time - o.end_time;
    }
}

public class BOJ17612_쇼핑몰 {
    public static void main(String[] args) throws IOException {
        // 기본 입력 받기 / 기본 선언(cnt/result)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N, k, cnt=1;
        long result=0;
        PriorityQueue<Counter> calculating =new PriorityQueue<>();
        ArrayList<Customer> customers = new ArrayList<>();

        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        k = Integer.parseInt(temp[1]);

        // 계산대 세팅
        for (int id=1; id<=k; id++) {
            calculating.offer(new Counter(id));
        }

        // N번 돌면서 계산 돌리기
        for (int n=0; n<N; n++) {
            temp = br.readLine().split(" ");
            int id = Integer.parseInt(temp[0]);
            int w = Integer.parseInt(temp[1]);

            Counter counter = calculating.poll();

            counter.user = id;
            counter.end_time += w;
            calculating.offer(counter);
            customers.add(new Customer(counter.user, counter.end_time, counter.id));
        }

        Collections.sort(customers);
        for (Customer c : customers) {
            result += (long) c.id*cnt;
            cnt++;
        }
        System.out.println(result);
    }
}
