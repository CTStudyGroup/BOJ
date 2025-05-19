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

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M, K, result;
int graph[101][101];
bool visited[101][101];

int bfs(int x, int y) {
    queue<pii> q;
    q.push(make_pair(x, y));
    visited[x][y] = true;
    int cnt = 1;

    while(!q.empty()) {
        int xx = q.front().first;
        int yy = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++) {
            int nx = xx + dx[i];
            int ny = yy + dy[i];

            if(nx > 0 && nx <= N && ny > 0 && ny <= M) {
                if(!visited[nx][ny] && graph[nx][ny] == 1) {
                    q.push(make_pair(nx, ny));
                    visited[nx][ny] = true;
                    cnt++;
                }
            }
        }
    }

    return cnt;
}

void solve() {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
            if(graph[i][j] == 1) {
                result = max(result, bfs(i, j));
            }
        }
    }

    cout << result;
}

void input() {
    cin >> N >> M >> K;

    for(int i = 0; i < K; i++) {
        int a, b;
        cin >> a >> b;
        graph[a][b] = 1;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
