package 백준;

import java.io.*;
import java.util.*;

public class 등산 {
    static int N,M,T,D;
    static int[][] map;
    static int[][] go;
    static int[][] back;
    static int[] dy={-1,1,0,0};
    static int[] dx={0,0,-1,1};
    static class Node implements Comparable<Node>{
        int y,x,time;

        Node(int y,int x,int time){
            this.y=y;
            this.x=x;
            this.time=time;
        }

        @Override
        public int compareTo(Node n){
            return this.time-n.time;
        }
    }

    static PriorityQueue<Node> q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        T=Integer.parseInt(st.nextToken());
        D=Integer.parseInt(st.nextToken());

        map=new int[N][M];
        go=new int[N][M];
        back=new int[N][M];

        // 입력 및 초기화
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                char c = line.charAt(j);
                if(Character.isUpperCase(c)) map[i][j] = c - 'A';
                else map[i][j] = c - 'a' + 26;

                go[i][j]=Integer.MAX_VALUE;
                back[i][j]=Integer.MAX_VALUE;
            }
        }

        // go 초기화: 시작점 거리 설정
        q=new PriorityQueue<>();
        go[0][0] = 0;
        q.offer(new Node(0,0,0));

        BFS_go(); // 호텔에서 모든 산에 가는 가장 적은 시간을 구함

        // back: 호텔에서 역방향 비용으로 다익스트라 (간선 뒤집기)
        BFS_back();

        int answer=0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(go[i][j]==Integer.MAX_VALUE || back[i][j]==Integer.MAX_VALUE) continue;
                int total=back[i][j]+go[i][j];
                if(total<=D) answer=Math.max(answer,map[i][j]);
            }
        }

        System.out.println(answer);
    }

    // 정방향 다익스트라 (0,0 -> 모든 칸)
    public static void BFS_go(){
        while (!q.isEmpty()){
            Node n=q.poll();

            // 이미 더 짧은 경로가 발견된 노드면 건너뜀 (다익스트라 표준)
            if(n.time > go[n.y][n.x]) continue;

            for (int d = 0; d < 4; d++) {
                int ny=dy[d]+n.y;
                int nx=dx[d]+n.x;

                if(0<=ny && 0<=nx && ny<N && nx<M){
                    int tmp=Math.abs(map[ny][nx]-map[n.y][n.x]);// 높이 차이

                    if(tmp > T) continue; // 이동 불가

                    int total_time=n.time;
                    if(map[n.y][n.x] >= map[ny][nx]) total_time += 1;
                    else total_time += tmp * tmp;

                    if(total_time < go[ny][nx]){
                        go[ny][nx]=total_time;
                        q.offer(new Node(ny,nx,total_time));
                    }
                }
            }
        }
    }

    // 역방향 다익스트라: 호텔에서 출발해서 "역방향 비용"으로 이동
    static void BFS_back(){
        q = new PriorityQueue<>();
        q.add(new Node(0, 0, 0));
        back[0][0] = 0;

        while(!q.isEmpty()){
            Node n = q.poll();

            if(n.time > back[n.y][n.x]) continue;

            for(int d=0;d<4;d++){
                int ny = n.y + dy[d];
                int nx = n.x + dx[d];

                if(ny<0||nx<0||ny>=N||nx>=M) continue;

                int diff = Math.abs(map[ny][nx] - map[n.y][n.x]);
                if(diff > T) continue;

                // 역방향 비용 계산: (현재 n은 '호텔에서 출발한' 정점)
                // cost = 원래(next -> cur) 비용
                int cost;
                if(map[n.y][n.x] <= map[ny][nx]) cost = 1;
                else {
                    int hd = map[n.y][n.x] - map[ny][nx];
                    cost = hd * hd;
                }

                int nt = n.time + cost;

                if(nt < back[ny][nx]){
                    back[ny][nx] = nt;
                    q.add(new Node(ny, nx, nt));
                }
            }
        }
    }
}
