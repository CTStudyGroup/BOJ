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
char graph[13][7];
bool visited[13][7];
bool flag;
int cnts;

void bfs(int a, int b) {
    queue<pii> q;
    visited[a][b] = true;
    int cnt = 1;
    vector<pii> tmp;
    tmp.push_back({a, b});
    q.push({a, b});

    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || nx >= 12 || ny < 0 || ny >= 6) continue;

            if(!visited[nx][ny] && graph[nx][ny] == graph[x][y]) {
                q.push({nx, ny});
                tmp.push_back({nx, ny});
                visited[nx][ny] = true;
                cnt++;
            }
        }
    }

    if(cnt >= 4) {      // 없앨 수 있음
        flag = true;
        for(auto it : tmp) {
            int x = it.first;
            int y = it.second;

            graph[x][y] = '.';
        }
    }
}

void Print() {
    for(int i = 0; i < 12; i++) {
        for(int j = 0; j < 6; j++) {
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }
}

void down() {
    for(int j = 0; j < 6; j++) {
        vector<char> tmp;
        for(int i = 11; i >= 0; i--) {
            if(graph[i][j] != '.') tmp.push_back(graph[i][j]);
        }

        int idx = 11;

        for(auto it : tmp) {
            graph[idx--][j] = it;
        }

        for(int i = idx; i >= 0; i--) {
            graph[i][j] = '.';
        }
    }
}

void solve() {
    while(true) {
        memset(visited, 0, sizeof(visited));
        flag = false;
        for(int i = 0; i < 12; i++) {
            for(int j = 0; j < 6; j++) {
                if(!visited[i][j] && graph[i][j] != '.') {
                    bfs(i, j);
                }
            }
        }
        // 아래로 이동
        down();

        if(!flag) {
            break;
        }
        cnts++;
    }
    cout << cnts;
}

void input() {
    for(int i = 0; i < 12; i++) {
        for(int j = 0; j < 6; j++) {
            cin >> graph[i][j];
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();

    return 0;
}
