#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e11

struct coordinate {
    int x;
    int y;
};

int dx[] = {0, 0, -1, 1, 1, -1, -1, 1};
int dy[] = {-1, 1, 0, 0, -1, 1, -1, 1};
int N, M;
int graph[101][101];
int visited[101][101];
int cnt = 0;

/*      0 -> 공기 , 1 -> 치즈
 *      0인 부분에서 bfs 시작
 */

bool check(int x, int y) {
    if(x >= 0 && x <= N && y >= 0 && y <= M) return true;
    return false;
}

void bfs() {
    queue<pii> q;
    q.push({1, 1});
    visited[1][1] = 1;

    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(check(nx, ny) && graph[nx][ny] == 0 && !visited[nx][ny]) {
                q.push({nx, ny});
                visited[nx][ny] = 1;
            }
            else if(check(nx, ny) && graph[nx][ny] == 1) {
                visited[nx][ny]++;
            }
        }
    }
}

void solve() {
    while(true) {
        memset(visited, 0, sizeof(visited));

        bfs();

        bool flag = false;
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                if (visited[i][j] >= 2) {
                    graph[i][j] = 0;
                    flag = true;
                }
            }
        }

        if (!flag) {
            cout << cnt;
            return;
        }
        cnt++;
    }
}

void input() {
    cin >> N >> M;

    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
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
