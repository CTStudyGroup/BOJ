#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    int y;
};

struct FISH {
    int x;
    int y;
    int Dir;
    bool live;
};

//int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
//int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int dx[] = {0, -1, -1, 0, 1, 1, 1, 0, -1};
int dy[] = {0,0, -1, -1, -1, 0, 1, 1, 1};
//int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
//int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
int graph[4][4];        // -1 : 상어가 있는 칸, 0 : 빈칸(상어 X, 물고기 X)
FISH Fish[17];          // 점수가 인덱스
int answer;


void Copy(int A[][4], int B[][4], FISH C[], FISH D[]) {
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            A[i][j] = B[i][j];
        }
    }

    for(int i = 1; i <= 16; i++) {
        C[i] = D[i];
    }
}

void Swap_Fish(int idx, int Idx) {
    FISH temp = Fish[idx];
    Fish[idx].x = Fish[Idx].x;
    Fish[idx].y = Fish[Idx].y;
    Fish[Idx].x = temp.x;
    Fish[Idx].y = temp.y;
}

void Move_Fish() {      // 물고기 움직이는 함수
    for(int i = 1; i <= 16; i++) {
        if(Fish[i].live == false) continue;

        int x = Fish[i].x;
        int y = Fish[i].y;
        int dirs = Fish[i].Dir;

        int nx = x + dx[dirs];
        int ny = y + dy[dirs];
        bool flag = false;

        if(nx >= 0 && nx < 4 && ny >= 0 && ny < 4) {
            if(graph[nx][ny] == 0) {        // 변경 없이 갈 수 있음
                flag = true;
                Fish[i].x = nx;
                Fish[i].y = ny;
                graph[nx][ny] = i;      // 다음 칸으로 이동
                graph[x][y] = 0;        // 이전 빈 칸으로 변경
            }
            else if(graph[nx][ny] != -1) {      // 기존처럼 변경하는 경우
                flag = true;
                Swap_Fish(i, graph[nx][ny]);
                swap(graph[x][y], graph[nx][ny]);
            }
        }

        if(flag == false) {         // 만약 발견하지 못한경우 반시계방향으로 찾아야함
            int nextDir = dirs + 1;
            if(nextDir == 9) nextDir = 1;
            nx = x + dx[nextDir];
            ny = y + dy[nextDir];

            while(nextDir != dirs) {
                if(nx >= 0 && nx < 4 && ny >= 0 && ny < 4) {
                    if(graph[nx][ny] == 0) {
                        Fish[i].x = nx;
                        Fish[i].y = ny;
                        graph[nx][ny] = i;
                        graph[x][y] = 0;
                        Fish[i].Dir = nextDir;
                        break;
                    }
                    else if(graph[nx][ny] != -1) {
                        Swap_Fish(i, graph[nx][ny]);
                        swap(graph[x][y], graph[nx][ny]);
                        Fish[i].Dir = nextDir;
                        break;
                    }
                }
                nextDir++;
                if(nextDir == 9) nextDir = 1;
                nx = x + dx[nextDir];
                ny = y + dy[nextDir];
            }
        }
    }
}

void Make_state(int x, int y, int nx, int ny, int Fish_num, bool isnum) {
    if(isnum == true) {     // 죽임
        graph[x][y] = 0;
        graph[nx][ny] = -1;
        Fish[Fish_num].live = false;
    }
    else {
        graph[x][y] = -1;
        graph[nx][ny] = Fish_num;
        Fish[Fish_num].live = true;
    }
}

void dfs(int x, int y, int dirs, int Sum) {
    answer = max(answer, Sum);

    int C_graph[4][4];
    FISH C_Fish[17];

    Copy(C_graph, graph, C_Fish, Fish);
    Move_Fish();

    for(int i = 1; i <= 3; i++) {
        int nx = x + dx[dirs] * i;
        int ny = y + dy[dirs] * i;

        if(nx >= 0 && nx < 4 && ny >= 0 && ny < 4) {
            if(graph[nx][ny] == 0) {
                continue;
            }

            int Fish_num = graph[nx][ny];
            int nDir = Fish[Fish_num].Dir;
            Make_state(x, y, nx, ny, Fish_num, true);
            dfs(nx, ny, nDir, Sum + Fish_num);
            Make_state(x, y, nx, ny, Fish_num, false);
        }
        else break;
    }
    Copy(graph, C_graph, Fish, C_Fish);
}

void solve() {
    int score = graph[0][0];
    int dir = Fish[score].Dir;
    Fish[score].live = false;
    graph[0][0] = -1;

    dfs(0, 0, dir, score);

    cout << answer;
}

void input() {
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            int a, b;
            cin >> a >> b;
            graph[i][j] = a;
            Fish[a] = {i, j, b, true};
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
