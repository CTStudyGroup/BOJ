#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define Endl "\n"
#define MAX 1e9

int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M;
char graph[251][251];
bool visited[251][251];
int wol, lam;

void bfs(int x, int y, int w, int l) {
    queue<pii> q;
    q.push(make_pair(x, y));
    visited[x][y] = true;
    int wl = w;
    int la = l;

    while(!q.empty()) {
        int xx = get<0>(q.front());
        int yy = get<1>(q.front());
        q.pop();

        for(int i = 0; i < 4; i++) {
            int nx = xx + dx[i];
            int ny = yy + dy[i];

            if(nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
            if(visited[nx][ny] || graph[nx][ny] == '#') continue;

            if(graph[nx][ny] == 'v') {
                q.push(make_pair(nx, ny));
                wl += 1;
                visited[nx][ny] = true;
            }
            else if(graph[nx][ny] == 'o') {
                q.push(make_pair(nx, ny));
                la += 1;
                visited[nx][ny] = true;
            }
            else {
                q.push(make_pair(nx, ny));
                visited[nx][ny] = true;
            }
        }
    }

    if(wl >= la) {
        wol += wl;
    }
    else lam += la;
}

void solve() {
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(!visited[i][j] && graph[i][j] == 'v') {
                bfs(i, j, 1, 0);
            }
            else if(!visited[i][j] && graph[i][j] == 'o') {
                bfs(i, j, 0, 1);
            }
            else if(!visited[i][j] && graph[i][j] == '.') {
                bfs(i, j, 0, 0);
            }
        }
    }

    cout << lam << " " << wol;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
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

