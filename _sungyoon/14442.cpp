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

int dx[] = {0, -1, 0, 1, 1, -1, -1, 1};
int dy[] = {-1, 0, 1, 0, -1, 1, -1, 1};
int N, M, K;
int graph[1001][1001];
bool visited[1001][1001][10];

void bfs() {
    queue<tuple<int, int, int, int>> q;
    q.push({0, 0, 0, 0});
    visited[0][0][0] = true;

    while(!q.empty()) {
        int x = get<0>(q.front());
        int y = get<1>(q.front());
        int status = get<2>(q.front());
        int dist = get<3>(q.front());
        q.pop();

        if(x == N-1 && y == M-1) {
            cout << dist + 1;
            exit(0);
        }

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

            if(visited[nx][ny][status]) continue;

            if(graph[nx][ny] == 1) {        //  장애물이 있는 경우 
                if(status + 1 > K) {        // 갈 수 없음
                    continue;
                }
                else {
                    q.push({nx, ny, status+1, dist+1});
                    visited[nx][ny][status+1] = true;
                }
            }
            else {
                q.push({nx, ny, status, dist+1});
                visited[nx][ny][status] = true;
            }
        }
    }
}

void solve() {
    bfs();

    cout << -1;
}

void input() {
    cin >> N >> M >> K;

    for(int i = 0; i < N; i++) {
        string s;
        cin >> s;
        for(int j = 0; j < M; j++) {
            graph[i][j] = s[j] - '0';
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
