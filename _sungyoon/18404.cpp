#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    int y;
    int r;
};

struct horse {
    int x;
    int y;
    int dir;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
// int dx[] = {0, 0, 1, -1};
// int dy[] = {1, -1, 0, 0};
int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
int N, M, x1, x2;
vector<pii> v;
int graph[501][501];        // 1은 나이트, 2는 기물
int dist[501][501];

void dijkstra(int x1, int x2) {
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
    dist[x1][x2] = 0;
    pq.push({0, x1, x2});       // 움직인 횟수, 좌표

    while(!pq.empty()) {
        int cost = get<0>(pq.top());
        int x = get<1>(pq.top());
        int y = get<2>(pq.top());
        pq.pop();

        if(cost > dist[x][y]) continue;

        for(int i = 0; i < 8; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx <= 0 || nx > N || ny <= 0 || ny > N) continue;

            if(dist[nx][ny] > cost + 1) {
                pq.push({cost+1, nx, ny});
                dist[nx][ny] = cost+1;
            }
        }
    }
}

void solve() {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            dist[i][j] = MAX;
        }
    }

    dijkstra(x1, x2);

    for(auto it : v) {
        cout << dist[it.first][it.second] << " ";
    }
}

void input() {
    cin >> N >> M;

    cin >> x1 >> x2;
    graph[x1][x2] = 1;

    for(int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        graph[a][b] = 2;
        v.push_back({a, b});
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

