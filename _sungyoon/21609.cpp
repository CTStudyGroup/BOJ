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

struct Customer {
    int x;
    int y;
    int Dest_x;
    int Dest_y;
};

int dx[] = {-1, 0, 0, 1, 1, -1, -1, 1};
int dy[] = {0, -1, 1, 0, -1, 1, -1, 1};
//int dx[] = {0, -1, -1, 0, 1, 1, 1, 0, -1};
//int dy[] = {0,0, -1, -1, -1, 0, 1, 1, 1};
//int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
//int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
int graph[21][21];
bool visited[21][21];
int N, M, result, max_score, startx, starty, tmprain;
vector<tuple<int, int, int, int>> v;

/*
 * 검은색 블록, -1, 무지개 블록 0, 나머지 종류가 M인 일반 블록
 * 블록 그룹에는 일반 블록이 하나 이상 존재, 포함된 일반 블록의 색은 같아야함, 무지개 블록은 상관없음, 블록의 개수는 2보다 커야함
*/

bool compare(tuple<int, int, int, int> a, tuple<int, int, int, int> b) {
    if(get<0>(a) != get<0>(b)) return get<0>(a) > get<0>(b);
    if(get<1>(a) != get<1>(b)) return get<1>(a) > get<1>(b);
    if(get<2>(a) != get<2>(b)) return get<2>(a) > get<2>(b);
    return get<3>(a) > get<3>(b);
}

void bfs(int x, int y, int color) {
    bool tmp_visited[21][21];
    memset(tmp_visited, 0, sizeof(tmp_visited));
    queue<tuple<int, int, int>> q;
    tmp_visited[x][y] = true;
    q.push({x, y, graph[x][y]});
    vector<pii> group;
    group.push_back({x,y});
    int rainbow = 0;
    int cnt = 1;

    while(!q.empty()) {
        int xx = get<0>(q.front());
        int yy = get<1>(q.front());
        int cl = get<2>(q.front());
        q.pop();

        for(int i = 0; i < 4; i++) {
            int nx = xx + dx[i];
            int ny = yy + dy[i];

            if(nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

            if(tmp_visited[nx][ny] || graph[nx][ny] == -1) continue;

            if(color == graph[nx][ny] || graph[nx][ny] == 0) {
                if(graph[nx][ny] == 0) {
                    rainbow++;
                }
                q.push({nx, ny, graph[nx][ny]});
                group.push_back({nx, ny});
                tmp_visited[nx][ny] = true;
                cnt++;
            }
        }
    }

    int standx = -1;
    int standy = -1;

    for(auto it : group) {
        int i = it.first;
        int j = it.second;

        if(graph[i][j] == 0) continue;

        if(standx == -1 || i > standx || (i == standx && j < standy)) {
            standx = i;
            standy = j;
        }
        visited[i][j] = true;
    }

    if(cnt < 2) return;
    v.push_back({cnt, rainbow, x, y});
}

void bfs1(int x, int y, int color) {
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            visited[i][j] = false;
        }
    }
    queue<tuple<int, int, int>> q;
    visited[x][y] = true;
    q.push({x, y, graph[x][y]});
    graph[x][y] = -2;

    while(!q.empty()) {
        int xx = get<0>(q.front());
        int yy = get<1>(q.front());
        int cl = get<2>(q.front());
        q.pop();

        for(int i = 0; i < 4; i++) {
            int nx = xx + dx[i];
            int ny = yy + dy[i];

            if(nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

            if(visited[nx][ny] || graph[nx][ny] == -1) continue;

            if(color == graph[nx][ny] || graph[nx][ny] == 0) {
                q.push({nx, ny, graph[nx][ny]});
                graph[nx][ny] = -2;
                visited[nx][ny] = true;
            }
        }
    }
}

void gravity() {
    for(int i = N-2; i >= 0; i--) {
        for(int j = 0; j < N; j++) {
            if(graph[i][j] == -2) continue;
            if(graph[i][j] == -1) continue;

            int color = graph[i][j];
            int nx = i + 1;

            while(true) {
                if(nx == N) break;
                if(graph[nx][j] != -2) break;
                nx++;
            }
            nx--;

            graph[i][j] = -2;
            graph[nx][j] = color;
        }
    }
}

void rotation() {
    int tmpgraph[21][21];

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            tmpgraph[i][j] = graph[i][j];
        }
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            graph[i][j] = tmpgraph[j][N-1-i];
        }
    }
}

void solve() {
    while(true) {
        memset(visited, 0, sizeof(visited));
        v.clear();
        for(int i = 0; i < N; i++) {            // 최대 점수 찾기
            for(int j = 0; j < N; j++) {
                if(graph[i][j] != -1 && graph[i][j] != 0 && graph[i][j] != -2 && !visited[i][j]) {
                    bfs(i, j, graph[i][j]);
                }
            }
        }

        if(v.empty()) break;

        sort(v.begin(), v.end(), compare);
        startx = get<2>(v[0]);
        starty = get<3>(v[0]);
        int tmpcnt = get<0>(v[0]);
        bfs1(startx, starty, graph[startx][starty]);     // 최댓값 요소들 제거 -> -2로 변경
        result += tmpcnt * tmpcnt;
        gravity();          // 중력
        rotation();
        gravity();
    }
    cout << result;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> graph[i][j];
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
