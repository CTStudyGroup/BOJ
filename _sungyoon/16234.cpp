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

int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, L, R;
int graph[51][51];
int visited[51][51];
int arr[2501];
int countarr[2501];
int tmp = 1;
bool flag = false;

pii bfs(int a, int b) {
    queue<pii> q;
    int value = graph[a][b];
    q.push({a, b});
    visited[a][b] = tmp;
    int cnt = 1;

    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

            if(!visited[nx][ny] && abs(graph[x][y] - graph[nx][ny]) >= L && abs(graph[x][y] - graph[nx][ny]) <= R) {
                q.push({nx, ny});
                value += graph[nx][ny];
                visited[nx][ny] = tmp;
                flag = true;
                cnt++;
            }
        }
    }

    return {value, cnt};
}

void solve() {
    int cnt = 0;
    while(true) {
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(!visited[i][j]) {
                    pii val = bfs(i, j);
                    arr[tmp] = val.first;
                    countarr[tmp] = val.second;
                    tmp++;
                }
            }
        }

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(visited[i][j] > 0) {
                    graph[i][j] = arr[visited[i][j]] / countarr[visited[i][j]];
                }
            }
        }

        if(!flag) {
            break;
        }
        cnt++;
        memset(visited, 0, sizeof(visited));
        memset(arr, 0, sizeof(arr));
        tmp = 1;
        flag = false;
    }

    cout << cnt;
}

void input() {
    cin >> N >> L >> R;
    for(int i = 0; i < N; i++) {
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

