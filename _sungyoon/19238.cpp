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
int N, M, fuel, startx, starty, endx, endy;
int graph[21][21];      // 홀수 번호 손님 위치, 짝수 번호 도착지
bool visited[21][21];
int destination;
Customer customer[401];

bool compare(tuple<int, int, int> a, tuple<int, int, int> b) {
    if (get<0>(a) != get<0>(b)) return get<0>(a) < get<0>(b);
    if (get<1>(a) != get<1>(b)) return get<1>(a) < get<1>(b);
    return get<2>(a) < get<2>(b);
}

bool check() {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            if(graph[i][j] >= 1) return true;
        }
    }
    return false;
}

void Print() {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }
}

void bfs(int x, int y)  {       // 현재 택시에서 승객을 태울때
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            visited[i][j] = false;
        }
    }
    queue<tuple<int, int, int>> q;
    vector<tuple<int, int, int>> v;
    q.push({0, x, y});
    visited[x][y] = true;
    int min_dist = MAX;

    if(graph[x][y] > 0) {       // 현재 위치에 손님이 있는 경우
        endx = customer[graph[x][y]].Dest_x;
        endy = customer[graph[x][y]].Dest_y;
        graph[x][y] = 0;
        return;
    }

    while(!q.empty()) {
        int dst = get<0>(q.front());
        int xx = get<1>(q.front());
        int yy = get<2>(q.front());
        q.pop();

        if(min_dist != MAX && dst > min_dist) break;

        if(graph[xx][yy] > 0 && min_dist >= dst) {     // 승객을 태웠을때
            v.push_back({dst, xx, yy});
        }

        for(int i = 0; i < 4; i++) {
            int nx = xx + dx[i];
            int ny = yy + dy[i];

            if(nx > N || nx <= 0 || ny > N || ny <= 0) continue;

            if(visited[nx][ny] || graph[nx][ny] == -1) continue;

            q.push({dst+1, nx, ny});
            visited[nx][ny] = true;
        }
    }

    if(v.empty()) {     // 태울 사람 없음
        if(check()) {       // 사람이 있는 경우
            cout << -1;
        }
        else cout << fuel;
        exit(0);
    }
    sort(v.begin(), v.end(), compare);
    fuel -= get<0>(v[0]);
    if(fuel < 0) {      // 연료가 없는 경우
        cout << -1;
        exit(0);
    }
    startx = get<1>(v[0]);          // 시작 위치 재조정
    starty = get<2>(v[0]);
    endx = customer[graph[startx][starty]].Dest_x;      // 도착 위치 재조정
    endy = customer[graph[startx][starty]].Dest_y;
    graph[startx][starty] = 0;
}

void bfs1(int x, int y) {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            visited[i][j] = false;
        }
    }
    queue<tuple<int, int, int>> q;
    q.push({0, x, y});
    if(x == endx && y == endy) {        // 시작점과 도착점이 같은 경우
        return;
    }

    visited[x][y] = true;

    while(!q.empty()) {
        int dist = get<0>(q.front());
        int xx = get<1>(q.front());
        int yy = get<2>(q.front());
        q.pop();

        if(xx == endx && yy == endy) {      // 목적지에 도착한 경우
            fuel -= dist;

            if(fuel < 0) {
                cout << -1;
                exit(0);
            }
            fuel += dist * 2;
            startx = xx;
            starty = yy;
            return;
        }

        for(int i = 0; i < 4; i++) {
            int nx = xx + dx[i];
            int ny = yy + dy[i];

            if(nx > N || nx <= 0 || ny > N || ny <= 0) continue;

            if(graph[nx][ny] == -1 || visited[nx][ny]) continue;

            q.push({dist+1, nx, ny});
            visited[nx][ny] = true;
        }
    }

    cout << -1;
    exit(0);
}

void solve() {
    while(check()) {
        bfs(startx, starty);
        bfs1(startx, starty);
    }

    cout << fuel;
}

void input() {
    cin >> N >> M >> fuel;

    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            cin >> graph[i][j];

            if(graph[i][j] == 1) graph[i][j] = -1;      // 장애물
        }
    }

    cin >> startx >> starty;

    graph[startx][starty] = -2;

    for(int i = 1; i <= M; i++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        customer[i] = {a, b, c, d};
        graph[a][b] = i;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
