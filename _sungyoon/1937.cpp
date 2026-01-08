#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

struct Tree {
    int Node, left, right;
};

const int INF = 1e9;
const int MAX = 123457;
const int MOD = 1e9 + 7;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int N;
int graph[501][501];
int dp[501][501];

int func(int x, int y) {
    if(x >= N || x < 0 || y >= N || y < 0) return 0;
    int &ret = dp[x][y];

    if(ret != 0) {
        return ret;
    }

    ret = 1;

    for(int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx >= N || nx < 0 || ny >= N || ny < 0) continue;

        if(graph[x][y] < graph[nx][ny]) {
            ret = max(ret, func(nx, ny) + 1);
        }
    }

    return ret;
}

void solve() {
    int answer = 0;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            if(dp[i][j] == 0) {
                answer = max(func(i, j), answer);
            }
        }
    }

    cout << answer;
}

void input() {
    cin >> N;

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
