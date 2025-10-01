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

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dx[] = {-2, -2, 0, 0, 2, 2};
int dy[] = {-1, 1, -2, 2, -1, 1};
int N, r1, c1, r2, c2;
bool visited[201][201];

void bfs(int a, int b) {
    queue<tuple<int, int, int>> q;
    q.push({a, b, 0});
    visited[a][b] = true;

    while(!q.empty()) {
        int x = get<0>(q.front());
        int y = get<1>(q.front());
        int cnt = get<2>(q.front());
        q.pop();

        if(x == r2 && y == c2) {
            cout << cnt;
            exit(0);
        }

        for(int i = 0; i < 6; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

            if(!visited[nx][ny]) {
                q.push({nx, ny, cnt+1});
                visited[nx][ny] = true;
            }
        }
    }
}

void solve() {
    bfs(r1, c1);

    cout << -1;
}

void input() {
    cin >> N;

    cin >> r1 >> c1 >> r2 >> c2;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

