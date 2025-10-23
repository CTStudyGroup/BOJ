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

struct horse {
    int x;
    int y;
    int dir;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
// int dx[] = {0, 0, 1, -1};
// int dy[] = {1, -1, 0, 0};
int dx[] = {1, 0};
int dy[] = {0, 1};
int W, H;
ll dp[101][101][2][2];     // x, y, 이전에 왔던 방향, 회전 가능 불가
const int MOD = 100000;

void solve() {
    for(int i = 1; i < W; i++) {
        dp[i][0][0][1] = 1;
    }

    for(int i = 1; i < H; i++) {
        dp[0][i][1][1] = 1;
    }

    for(int i = 1; i < W; i++) {
        for(int j = 1; j < H; j++) {
            dp[i][j][0][0] = dp[i-1][j][1][1] % MOD;
            dp[i][j][0][1] = (dp[i-1][j][0][0] + dp[i-1][j][0][1]) % MOD;
            dp[i][j][1][0] = dp[i][j-1][0][1] % MOD;      // 아래에서 왔고 방향을 바꿨으니 회전 불가
            dp[i][j][1][1] = (dp[i][j-1][1][0] + dp[i][j-1][1][1]) % MOD;
        }
    }

    ll answer = 0;

    for(int i = 0; i < 2; i++) {
        for(int j = 0; j < 2; j++) {
            answer = (answer + dp[W-1][H-1][i][j]) % MOD;
        }
    }

    cout << answer;
}

void input() {
    cin >> W >> H;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

