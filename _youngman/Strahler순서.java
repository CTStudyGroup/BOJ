package 백준;

import java.io.*;
import java.util.*;

public class Strahler순서 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T=Integer.parseInt(st.nextToken());

        for (int tc = 0; tc < T; tc++) {
            st=new StringTokenizer(br.readLine());
            int K=Integer.parseInt(st.nextToken());
            int M=Integer.parseInt(st.nextToken());
            int P=Integer.parseInt(st.nextToken());

            List<Integer>[] list=new List[M+1];
            int[] degree=new int[M+1];
            int[] max=new int[M+1];
            int[] cnt=new int[M+1];
            int[] strahler=new int[M+1];

            for (int i = 1; i <= M; i++) {
                list[i]=new ArrayList();
            }

            for (int i = 0; i < P; i++) {
                st=new StringTokenizer(br.readLine());
                int p=Integer.parseInt(st.nextToken());
                int c=Integer.parseInt(st.nextToken());

                list[p].add(c);
                degree[c]+=1;
            }

            Queue<Integer> q=new ArrayDeque<>();

            for (int i = 1; i <=M ; i++) {
                if (degree[i]==0){
                    q.offer(i);
                    strahler[i]=1;
                }
            }

            while (!q.isEmpty()){
                int now=q.poll();

                for (int i = 0; i < list[now].size(); i++) {
                    int next=list[now].get(i);

                    if(strahler[now]>max[next]){
                        max[next]=strahler[now];
                        cnt[next]=1;
                    }else if(strahler[now]==max[next]){
                        cnt[next]+=1;
                    }

                    degree[next]-=1;

                    if(degree[next]==0){
                        if (cnt[next] >= 2) {
                            strahler[next] = max[next] + 1;
                        } else {
                            strahler[next] = max[next];
                        }
                        q.offer(next);
                    }
                }
            }

            System.out.println(K + " " + strahler[M]);
        }
    }
}
