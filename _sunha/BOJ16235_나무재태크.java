import java.io.*;
import java.util.*;

public class BOJ16235_나무재태크 {
    static int N,M,K;
    static int[][] A, land;
    static Deque<Tree> trees;
    static Deque<Tree> dead_trees = new ArrayDeque<>();
    static Deque<Tree> new_trees = new ArrayDeque<>();
    static int[][] ofs = new int[][] {{-1,-1}, {-1,0}, {-1,1}, {0,-1}, {0,1}, {1,-1}, {1,0}, {1,1}};

    static class Tree implements Comparable<Tree>{
        int x, y, age;

        public Tree(int x, int y, int age) {
            this.x = x;
            this.y = y;
            this.age = age;
        }


        @Override
        public int compareTo(Tree o) {
            return this.age-o.age;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        M = Integer.parseInt(temp[1]);
        K = Integer.parseInt(temp[2]);

        A = new int[N][N];
        land = new int[N][N];
        for (int r=0; r<N; r++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int c=0; c<N; c++) {
                A[r][c] = Integer.parseInt(st.nextToken());
                land[r][c] = 5;
            }
        }

        int x,y,z;
        List<Tree> temp_list = new ArrayList<>();
        for (int m=0; m<M; m++) {
            temp = br.readLine().split(" ");
            x = Integer.parseInt(temp[0])-1;
            y = Integer.parseInt(temp[1])-1;
            z = Integer.parseInt(temp[2]);

            temp_list.add(new Tree(x,y,z));
        }

        Collections.sort(temp_list);
        trees = new ArrayDeque<>(temp_list);


        // 시뮬레이션
        Tree tree;
        int age;
        // K > 0 일 때까지 반복
        for (int k=0; k<K; k++) {
            // 봄
            // M 값 수정
            M = trees.size();

            for (int m=0; m<M; m++){
                tree = trees.poll();
                x = tree.x;
                y = tree.y;
                age = tree.age;

                if (land[x][y] >= age){ // - 양분 / + 나이 후 push
                    land[x][y] -= age;
                    tree.age += 1;
                    trees.offer(tree);

                    if (tree.age % 5 == 0){
                        new_trees.offer(tree);
                    }

                } else {                // 여름 작업을 위해 죽은 나무 추가.
                    dead_trees.offer(tree);
                }
            }

            // 여름: 사망한 나무 -> 양분
            while (!dead_trees.isEmpty()) {
                tree = dead_trees.poll();
                x = tree.x;
                y = tree.y;
                age = tree.age;

                land[x][y] += age/2;
            }

            // 가을: 나무 번식
            while (!new_trees.isEmpty()){
                tree = new_trees.poll();
                x = tree.x;
                y = tree.y;

                for (int[] o: ofs) {
                    int nx = x + o[0];
                    int ny = y + o[1];

                    if (nx>=0 && nx<N && ny>=0 && ny<N) {
                        trees.offerFirst(new Tree(nx, ny, 1));  // 맨 앞에 넣어서 정렬 맞춰줘야함.
                    }
                }
            }

            // 겨울: 양분 +
            for (int r=0; r<N; r++) {
                for (int c=0; c<N; c++) {
                    land[r][c] += A[r][c];
                }
            }
        }
        System.out.println(trees.size());
    }
}