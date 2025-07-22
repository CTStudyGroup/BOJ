#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int N, M, K, lens, cnt;
char graph[101][101];
int dp[101][101][81];
string s;

int dfs(int x, int y, int idx) {
    if(dp[x][y][idx] != -1) return dp[x][y][idx];

    if(idx == lens-1) return 1;

    dp[x][y][idx] = 0;

    int& ret = dp[x][y][idx];

    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < K; j++) {
            int nx = x + dx[i] * (j + 1);
            int ny = y + dy[i] * (j + 1);

            if(nx >= N || nx < 0 || ny >= M || ny < 0) continue;

            if(graph[nx][ny] == s[idx+1]) {
                ret += dfs(nx, ny, idx+1);
            }
        }
    }

    return ret;
}

void solve() {
    memset(dp, -1, sizeof(dp));

    lens = s.length();

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(graph[i][j] == s[0]) {
                cnt += dfs(i, j, 0);
            }
        }
    }

    cout << cnt;
}

void input() {
    cin >> N >> M >> K;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cin >> graph[i][j];
        }
    }

    cin >> s;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
