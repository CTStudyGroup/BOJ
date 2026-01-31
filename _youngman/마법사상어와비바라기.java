package 백준;

import java.io.*;
import java.util.*;

public class 마법사상어와비바라기 {
    static int[] dy={0,-1,-1,-1,0,1,1,1};
    static int[] dx={-1,-1,0,1,1,1,0,-1};
    static int N,M;
    static int[][] map;
    static List<int[]> groom=new ArrayList<>();
    static boolean[][] use;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());

        map=new int[N][N];

        for (int i = 0; i < N; i++) {
            st=new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        groom.add(new int[] {N-1,0});
        groom.add(new int[] {N-1,1});
        groom.add(new int[] {N-2,0});
        groom.add(new int[] {N-2,1});

        for (int i = 0; i < M; i++) {
            st=new StringTokenizer(br.readLine());
            int d=Integer.parseInt(st.nextToken());
            int s=Integer.parseInt(st.nextToken());
            use=new boolean[N][N];

            move_groom(d-1,s);

            // 구름이 있는 칸에 비가 내림
            for (int j = 0; j < groom.size(); j++) {
                int[] yx=groom.get(j);
                map[yx[0]][yx[1]]+=1;
                use[yx[0]][yx[1]]=true;
            }

            // 물 복사 버그 실행
            water_bug();

            // 물의 양이 2이상인 모든 칸에 구름 생성
            groom=new ArrayList<>();
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    if(map[j][k]>=2 && !use[j][k]){
                        groom.add(new int[] {j,k});
                        map[j][k]-=2;
                    }
                }
            }
        }

        int answer=0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                answer+=map[i][j];
            }
        }

        System.out.println(answer);
    }

    public static void move_groom(int d,int s){
        for (int i = 0; i < s; i++) {
            List<int[]> tmp_groom=new ArrayList<>();

            for (int j = 0; j < groom.size(); j++) {
                int[] yx=groom.get(j);
                int ny=yx[0]+dy[d];
                int nx=yx[1]+dx[d];

                if(ny>=N) ny=0;
                if(nx>=N) nx=0;
                if(ny<0)ny=N-1;
                if(nx<0)nx=N-1;

                tmp_groom.add(new int[] {ny,nx});
            }

            groom=new ArrayList<>();
            for (int j = 0; j < tmp_groom.size(); j++) {
                groom.add(new int[] {tmp_groom.get(j)[0],tmp_groom.get(j)[1]});
            }
        }
    }

    public static void water_bug(){
        for (int i = 0; i < groom.size(); i++) {
            int[] yx=groom.get(i);
            int sum=0;

            for (int j = 0; j < 8; j++) {
                if(j%2!=0){
                    int ny=yx[0]+dy[j];
                    int nx=yx[1]+dx[j];

                    if(0<=ny && 0<=nx && ny<N && nx<N && map[ny][nx]>0){
                        sum+=1;
                    }
                }
            }

            map[yx[0]][yx[1]]+=sum;
        }
    }
}
