#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {0, 1, 1, 1, 0, 0, 0, -1, -1, -1};
int dy[] = {0, -1, 0, 1, -1, 0, 1, -1, 0, 1};
int R, C;
int graph[101][101];
int tmpgraph[101][101];
pii start;
string s;

int manhatan(int x, int y) {
    int dist = 1e9;      // 거리
    int direct = 0;       // 어느 방향

    for(int i = 1; i <= 9; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx >= 0 && ny >= 0 && nx < R && ny < C) {
            int tmpdist = abs(start.first - nx) + abs(start.second - ny);

            if(tmpdist < dist) {
                dist = tmpdist;
                direct = i;
            }
        }
    }
    return direct;
}

void solve() {
    for(int i = 0; i < s.length(); i++) {
        int stand = s[i] - '0';
        int xx = start.first + dx[stand];
        int yy = start.second + dy[stand];

        if(graph[xx][yy] != 2 && stand != 5) {        // 가려는 방향에 아두이노가 없는경우
            graph[xx][yy] = 1;
            graph[start.first][start.second] = 0;
            start.first = xx;
            start.second = yy;
        }
        else if(graph[xx][yy] == 2){
            cout << "kraj" << " " << i+1;
            exit(0);
        }

        vector<pii> crazy;

        // 그래프 탐색
        for(int j = 0; j < R; j++) {
            for(int k = 0; k < C; k++) {
                if(graph[j][k] == 2) {
                    crazy.push_back(make_pair(j, k));
                }
            }
        }

        for(auto &it : crazy) {
            int x = it.first;
            int y = it.second;
            int locate = manhatan(x, y);
            int nx = x + dx[locate];
            int ny = y + dy[locate];

            if(graph[nx][ny] == 1) {
                cout << "kraj" << " " << i+1;
                exit(0);
            }

            graph[nx][ny] = 2;
            graph[x][y] = 0;
            tmpgraph[nx][ny] += 1;
        }

        // 겹치는 아두이노 0으로 만들기
        for(int j = 0; j < R; j++) {
            for(int k = 0; k < C; k++) {
                if(tmpgraph[j][k] >= 2) {
                    graph[j][k] = 0;
                }
            }
        }

        memset(tmpgraph, 0, sizeof(tmpgraph));
    }
}

void input() {
    cin >> R >> C;

    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
            char a;
            cin >> a;
            if(a == 'I') {
                graph[i][j] = 1;
                start.first = i;
                start.second = j;
            }
            else if(a == '.') graph[i][j] = 0;
            else {
                graph[i][j] = 2;
            }
        }
    }

    cin >> s;
}

void result() {
    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
            if(graph[i][j] == 0) cout << '.';
            else if(graph[i][j] == 1) cout << 'I';
            else cout << 'R';
        }
        cout << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
    result();
}
