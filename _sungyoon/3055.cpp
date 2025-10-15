#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    string s;
    vector<int> v;
};

int dx[] = {-1, 0, 1, 0, 1, -1, -1, 1};
int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
int R, C;
char graph[51][51];
bool visited[51][51];
int startx, starty;
int endx, endy;
vector<pii> v;
queue<tuple<int, int, int>> q;

void water() {
    vector<pii> tmpv;

    for(auto it : v) {
        int x = it.first;
        int y = it.second;

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
            if(graph[nx][ny] == 'D' || graph[nx][ny] == 'X') continue;
            if(graph[nx][ny] == '*') continue;

            tmpv.push_back({nx, ny});
            graph[nx][ny] = '*';
        }
    }
    v = tmpv;
}

void bfs() {
    queue<tuple<int, int, int>> tmpq;
    while(!q.empty()) {
        int x = get<0>(q.front());
        int y = get<1>(q.front());
        int dst = get<2>(q.front());
        q.pop();

        if(graph[x][y] == '*') continue;

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || nx >= R || ny < 0 || ny >= C) continue;

            if(graph[nx][ny] == 'D') {
                cout << dst + 1;
                exit(0);
            }

            if(!visited[nx][ny] && graph[nx][ny] == '.') {
                tmpq.push({nx, ny, dst+1});
                visited[nx][ny] = true;
            }
        }
    }
    q = tmpq;
}

void solve() {
    while(!q.empty()) {
        bfs();
        water();
    }

    cout << "KAKTUS";
}

void input() {
    cin >> R >> C;

    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
            cin >> graph[i][j];

            if(graph[i][j] == 'S') {
                startx = i, starty = j;
                q.push({i, j, 0});
                visited[i][j] = true;
            }

            if(graph[i][j] == 'D') {
                endx = i, endy = j;
            }

            if(graph[i][j] == '*') {
                v.push_back({i, j});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
