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

struct halloween {
    int cnt;
    int score;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int M, N;
int graph[501][501];
int dp[501][501];

int ret(int x, int y) {
    if(x == M-1 && y == N-1) return 1;

    if(dp[x][y] != -1) {
        return dp[x][y];
    }

    dp[x][y] = 0;

    for(int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx >= 0 && nx < M && ny >= 0 && ny < N) {
            if(graph[x][y] > graph[nx][ny]) {
                dp[x][y] += ret(nx, ny);
            }
        }
    }

    return dp[x][y];
}

void solve() {
    memset(dp, -1, sizeof(dp));

    cout << ret(0, 0);
}

void input() {
    cin >> M >> N;

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

