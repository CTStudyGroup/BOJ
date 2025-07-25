#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

int dx[] = {-1, 0, 1, 0, 1, -1, -1, 1};
int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
int N, M, startx, starty;
char graph[501][501];
int visited[501][501][4];
char direct;
int result = -1;

int checkdir(int x, int y, int z) {
    if(graph[x][y] == '\\') {
        if(z == 0) {
            return 3;
        }
        else if(z == 1) {
            return 2;
        }
        else if(z == 2) {
            return 1;
        }
        else return 0;
    }

    if(graph[x][y] == '/') {
        if(z == 0) {
            return 1;
        }
        else if(z == 1) {
            return 0;
        }
        else if(z == 2) {
            return 3;
        }
        else return 2;
    }
    return z;
}

void bfs(int a, int b, int c) {
    queue<tuple<int, int, int, int>> q;     // x, y, 방향, 횟수
    q.push({a, b, c, 1});
    visited[a][b][c] = 1;

    while(!q.empty()) {
        int x = get<0>(q.front());
        int y = get<1>(q.front());
        int dir = get<2>(q.front());
        int cnt = get<3>(q.front());
        q.pop();

        int dirs = dir;

        if(graph[x][y] == '/' || graph[x][y] == '\\') {
            dirs = checkdir(x, y, dir);
        }

        int nx = x + dx[dirs];
        int ny = y + dy[dirs];

        if(nx > N || nx < 1 || ny > M || ny < 1 || graph[nx][ny] == 'C') {      // 그래프 밖으로 나간 경우
            if(result < cnt) {
                if(c == 0) {
                    direct = 'U';
                }
                else if(c == 1) {
                    direct = 'R';
                }
                else if(c == 2) {
                    direct = 'D';
                }
                else direct = 'L';
                result = cnt;
            }
            continue;
        }
        if(!visited[nx][ny][dirs]) {
            q.push({nx, ny, dirs, cnt+1});
            visited[nx][ny][dirs] = cnt+1;
        }
        else {
            if(c == 0) {
                cout << 'U' << endl;
            }
            else if(c == 1) cout << 'R' << endl;
            else if(c == 2) cout << 'D' << endl;
            else cout << 'L' << endl;

            cout << "Voyager";
            exit(0);
        }
    }
}

void solve() {
    for(int i = 0; i < 4; i++) {
        memset(visited, 0, sizeof(visited));
        bfs(startx, starty, i);

        if(result == -1) {
            if(i == 0) {
                cout << 'U' << endl;
            }
            else if(i == 1) cout << 'R' << endl;
            else if(i == 2) cout << 'D' << endl;
            else cout << 'L' << endl;

            cout << "Voyager";
            return;
        }
    }
    cout << direct << endl << result;
}

void input() {
    cin >> N >> M;

    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
            cin >> graph[i][j];
        }
    }

    cin >> startx >> starty;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
