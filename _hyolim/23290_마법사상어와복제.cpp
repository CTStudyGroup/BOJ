
#include <iostream>
#include <vector>
using namespace std;
#define MAX 5
 
int M, S;
int shark_y, shark_x;
int dy[] = { 0,-1,-1,-1,0,1,1,1 };
int dx[] = { -1,-1,0,1,1,1,0,-1 };
int s_dy[] = { 0,-1,0,1,0 };
int s_dx[] = { 0,0,-1,0,1 };
int smell[MAX][MAX];
vector<int> fish[MAX][MAX];
vector<int> copy_fish[MAX][MAX];
vector<int> shark_move;
int max_eat;
 
 
void copy_map(vector<int> a[][MAX], vector<int> b[][MAX]) {
    for (int i = 1; i < MAX; i++) {
        for (int j = 1; j < MAX; j++) {
            b[i][j] = a[i][j];
        }
    }
}
 
void move_fish(int time) {
    vector<int> new_fish[MAX][MAX];
	// 이차원 배열 탐색, 현재 물고기 있으면 물고기마다 위치 이동 및 이동 방향 재설정
    for (int i = 1; i < MAX; i++) {
        for (int j = 1; j < MAX; j++) {
            for (int k = 0; k < fish[i][j].size(); k++) {
                int y = i;
                int x = j;
                int dir = fish[i][j][k];
                      
                int ndir, ny, nx;
                bool flag = false;
                for (int i = 0; i < 8; i++) {
                    ndir = (8 + dir - i) % 8;
                    ny = y + dy[ndir];
                    nx = x + dx[ndir];
                    if (ny < 1 || nx < 1 || ny >= MAX || nx >= MAX)continue;
                    if (ny == shark_y && nx == shark_x)continue;
                    if (smell[ny][nx] != 0 && time-smell[ny][nx] <= 2)continue;
                    flag = true;
                    new_fish[ny][nx].push_back(ndir);
                    break;
                }
                if (!flag) {
                    new_fish[y][x].push_back(dir);
                }
            }
        }
    }
    copy_map(new_fish, fish);
}
 
int shark_simulation(vector<int> route) {
    bool visit[MAX][MAX] = { false, };
    int res = 0;
    int s_y = shark_y;
    int s_x = shark_x;
    for (auto dir : route) {
        s_y += s_dy[dir];
        s_x += s_dx[dir];
        if (s_y < 1 || s_x < 1 || s_y >= MAX || s_x >= MAX)return -1;
        if(!visit[s_y][s_x]){
            visit[s_y][s_x] = true;
            res += fish[s_y][s_x].size();
        }
    }
    return res;
}
// 상어 이동 시뮬레이션, 어디로 가는 것이 물고기를 최대로 먹을지
void search_best_move(vector<int> route) {
    if (route.size() == 3) {
    	// 3번 이동 했다면 물고기를 몇 마리 먹을 수 있는지 확인
        int eat = shark_simulation(route);
        if (eat > max_eat) {
            max_eat = eat;
            shark_move = route;
        }
        return;
    }
    for (int i = 1; i <= 4; i++) {
        route.push_back(i);
        search_best_move(route);
        route.pop_back();
    }
}
 
// 이동방향이 결정되었다면 상어 이동, 이동 중 물고기를 먹었다면 해당 위치에 냄새를 남김
void move_shark(int time) {
    for (auto dir : shark_move) {
        shark_y += s_dy[dir];
        shark_x += s_dx[dir];
        if (fish[shark_y][shark_x].size() != 0) {
            fish[shark_y][shark_x].clear();
            smell[shark_y][shark_x] = time;
        }
    }
}
 
void paste_fish() {
    for (int i = 1; i < MAX; i++) {
        for (int j = 1; j < MAX; j++) {
            for(auto dir:copy_fish[i][j]){
                fish[i][j].push_back(dir);
            }
        }
    }
}
 
int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(0);
    
    cin >> M >> S;
    int y, x, dir;
    for (int i = 1; i <= M; i++) {
        cin >> y >> x >> dir;
        fish[y][x].push_back(dir-1);
    }
    cin >> shark_y >> shark_x;
    
    for (int i = 1; i <= S; i++) {
    	//현재 물고기 위치 저장
        copy_map(fish, copy_fish);
        move_fish(i);
        // 상어 이동 시뮬레이션을 위한 설정, 상어 이동
        max_eat = -1;
        vector<int> temp;
        search_best_move(temp);
        move_shark(i);
        // 저장된 물고기 위치 복제
        paste_fish();
    }
    
	// 현재 남아 있는 물고기 수 
    int res = 0;
    for (int i = 1; i < MAX; i++) {
        for (int j = 1; j < MAX; j++) {
            res += fish[i][j].size();
        }
    }
    cout << res;
    return 0;
}