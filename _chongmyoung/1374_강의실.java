import java.util.*;

class Lecture implements Comparable<Lecture> {
    int s, e;
    Lecture(int s, int e) {
        this.s = s;
        this.e = e;
    }
    @Override
    public int compareTo(Lecture o) {
        return this.s - o.s; // 시작 시간 기준 오름차순
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Lecture> lectures = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            int number = sc.nextInt(); // 강의 번호 (사용하지 않음)
            int s = sc.nextInt();
            int e = sc.nextInt();
            lectures.add(new Lecture(s, e));
        }

        // 1. 시작 시간 기준 정렬
        Collections.sort(lectures);

        // 2. 최소 힙 (끝나는 시간 기준)
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        // 3. 첫 강의 배정
        pq.offer(lectures.get(0).e);

        // 4. 나머지 강의 배정
        for (int i = 1; i < n; i++) {
            // 가장 빨리 끝나는 강의보다 현재 강의 시작이 늦거나 같으면 → 재사용 가능
            if (pq.peek() <= lectures.get(i).s) {
                pq.poll();
            }
            pq.offer(lectures.get(i).e);
        }

        // 5. 필요한 강의실 수 = 큐 크기
        System.out.println(pq.size());
    }
}
