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
char graph[101][101];
bool visited[101][101];
int N, M, result1, result2;

int bfs(int x, int y) {
    queue<pii> q;
    int cnt = 1;
    q.push(make_pair(x, y));
    visited[x][y] = true;

    while(!q.empty()) {
        int xx = q.front().first;
        int yy = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++) {
            int nx = xx + dx[i];
            int ny = yy + dy[i];

            if(nx >= 0 && ny >= 0 && nx < M && ny < N) {
                if(!visited[nx][ny] && graph[xx][yy] == graph[nx][ny]) {
                    q.push(make_pair(nx, ny));
                    visited[nx][ny] = true;
                    cnt += 1;
                }
            }
        }
    }

    return cnt * cnt;
}

void solve() {
    for(int i = 0; i < M; i++) {
        for(int j = 0; j < N; j++) {
            if(graph[i][j] == 'W' && !visited[i][j]) {
                result1 += bfs(i, j);
            }
            else if(graph[i][j] == 'B' && !visited[i][j]) {
                result2 += bfs(i, j);
            }
        }
    }

    cout << result1 << " " << result2;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < M; i++) {
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
