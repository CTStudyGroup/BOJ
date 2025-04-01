#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M;
int graph[1001][1001];
bool visited[1001][1001];

void bfs(int x, int y) {
    queue<pii> q;

    q.push(make_pair(x, y));
    visited[x][y] = true;

    while(!q.empty()) {
        int xx = q.front().first;
        int yy = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++) {
            int nx = xx + dx[i];
            int ny = yy + dy[i];

            if(nx >= 0 && nx < N && ny >= 0 && ny < M) {
                if(!visited[nx][ny] && !graph[nx][ny]) {
                    q.push(make_pair(nx, ny));
                    visited[nx][ny] = true;
                }
            }
        }
    }
}

void solve() {
    for(int i = 0; i < 1; i++) {
        for(int j = 0; j < M; j++) {
            if(!visited[i][j] && !graph[i][j]) {
                bfs(i, j);
            }
        }
    }

    for(int i = 0; i < M; i++) {
        if(visited[N-1][i] && !graph[N-1][i]) {
            cout << "YES";
            return;
        }
    }

    cout << "NO";
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            char a;
            cin >> a;
            a = a - '0';
            graph[i][j] = a;
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

