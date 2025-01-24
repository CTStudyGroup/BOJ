#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>
#define fasti ios_base::sync_with_stdio(false); cin.tie(0);
#define fastio ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define INF 1e9+7
#define pii pair<int, int>
 
typedef long long ll;
// typedef pair<int, int> pii;
 
using namespace std;
 
struct Shark{
    int r, c, s, d, z;
};
 
struct Core{
    int s, d, z;
};
 
int R, C, M, ans;
vector<Shark> Sharks, tempsharks;
Core Map[101][101]; //상어의 크기만 가지고 있는 배열
// d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
int dr[5] = {0, -1, 1, 0, 0};
int dc[5] = {0, 0, 0, 1, -1};
 
void input(){
    int r, c, s, d, z;
    cin >> R >> C >> M;
    for(int i = 0; i < M; i++){
        cin >> r >> c >> s >> d >> z;
        Map[r][c] = {s, d, z};
    }
}
 
void fishing(int fisher){
    for(int r = 1; r <= R; r++){
        if(!Map[r][fisher].z) continue;
        ans += Map[r][fisher].z;
        Map[r][fisher] = {0, 0, 0};
        return;
    }
}
 
void ready_to_move(){
    Sharks.clear();
    for(int r = 1; r <= R; r++){
        for(int c = 1; c <= C; c++){
            if(!Map[r][c].z) continue;
            Sharks.push_back({r, c, Map[r][c].s, Map[r][c].d, Map[r][c].z});
        }
    }
}
 
void reset(){
    for (int r = 1; r <= R; r++){
        for (int c = 1; c <= C; c++){
            Map[r][c] = {0, 0, 0};
        }
    }
}
 
void move(vector<Shark> &temp, Shark &nowS){
    int speed = nowS.s;
    int dir = nowS.d;
    int nr = nowS.r;
    int nc = nowS.c;
    int dist;
    
    if(dir == 1 || dir == 2) dist = speed % ((R-1)*2);
    else if(dir == 3 || dir == 4) dist = speed % ((C-1)*2);
    
    while (dist){
        if(dir == 1){
            if(nr == 1){
                dir = 2;
                nr += dr[2];
            }
            else nr += dr[1];
        }
        else if(dir == 2){
            if(nr == R){
                dir = 1;
                nr += dr[1];
            }
            else nr += dr[2];
        }
        else if(dir == 3){
            if(nc == C){
                dir = 4;
                nc += dc[4];
            }
            else nc += dc[3];
        }
        else if(dir == 4){
            if(nc == 1){
                dir = 3;
                nc += dc[3];
            }
            else nc += dc[4];
        }
        dist--;
    }
    temp.push_back({nr, nc, speed, dir, nowS.z});
}
 
 
void shark_move(){
    //이동한 상어들의 임시공간
    tempsharks.clear();
    
    for(auto &now : Sharks){
        move(tempsharks, now);
    }
    
    reset();
    
    // 크기가 가장 큰 상어들만 남기는 작업
    for(auto &s : tempsharks){
        if(s.z > Map[s.r][s.c].z){
            Map[s.r][s.c] = {s.s, s.d, s.z};
        }
    }
}
 
void solve(){
    int fisher = 1;
    while(fisher <= C){
        fishing(fisher);
        ready_to_move();
        shark_move();
        fisher++;
    }
    
    cout << ans;
}
 
int main(){
    fasti
    input();
    solve();
    
    return 0;
}
 
Colored by Color Scripter