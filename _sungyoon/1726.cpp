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

//int dx[] = {-1, 0, 1, 0, 1, -1, -1, 1};
//int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
int dx[] = {0, 0, 0, 1, -1};
int dy[] = {0, 1, -1, 0, 0};
int M, N, startx, starty, startdir;
int graph[101][101];
bool visited[101][101][6];
int endx, endy, enddir;

bool check(int x, int y, int dirs) {
    if(x > 0 && x <= M && y > 0 && y <= N) {
        if(!visited[x][y][dirs] && graph[x][y] == 0) {
            return true;
        }
    }
    return false;
}

void bfs(int stx, int sty, int direc) {
    queue<tuple<int, int, int, int>> q;
    q.push({stx, sty, direc, 0});
    visited[stx][sty][direc] = true;

    while(!q.empty()) {
        int x = get<0>(q.front());
        int y = get<1>(q.front());
        int dir = get<2>(q.front());
        int cnt = get<3>(q.front());
        q.pop();

        if(x == endx && y == endy && dir == enddir) {
            cout << cnt;
            return;
        }

        if(dir == 1 || dir == 2) {
            for(int i = 3; i <= 4; i++) {
                if(check(x, y, i)) {
                    q.push({x, y, i, cnt+1});
                    visited[x][y][i] = true;
                }
            }
        } else if(dir == 3 || dir == 4) {
            for(int i = 1; i <= 2; i++) {
                if(check(x, y, i)) {
                    q.push({x, y, i, cnt+1});
                    visited[x][y][i] = true;
                }
            }
        }

        for(int i = 1; i <= 3; i++) {
            int nx = x + dx[dir] * i;
            int ny = y + dy[dir] * i;

            if (nx <= 0 || ny <= 0 || nx > M || ny > N) break;
            if (graph[nx][ny] == 1) break;
            if (visited[nx][ny][dir]) continue;

            q.push({nx, ny, dir, cnt+1});
            visited[nx][ny][dir] = true;
        }
    }
}

void solve() {
    bfs(startx, starty, startdir);
}

void input() {
    cin >> M >> N;

    for(int i = 1; i <= M; i++) {
        for(int j = 1; j <= N; j++) {
            cin >> graph[i][j];
        }
    }

    cin >> startx >> starty >> startdir;

    cin >> endx >> endy >> enddir;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
