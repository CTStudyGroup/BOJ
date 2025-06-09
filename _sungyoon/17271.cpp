#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e8

struct coordinate {
    int x;
    int y;
};

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int N, M;
ll dp[10001][101];
ll MOD = 1000000007;

void solve() {
    dp[0][1] = 1;

    for(int i = 1; i <= 10000; i++) {
        dp[i][1] = (dp[i-1][1] * 2) % MOD;
    }

    for(int i = 1; i <= 10000; i++) {
        for(int j = 1; j <= 100; j++) {
            if(i == j) dp[i][j] = 2;

            if(i < j) dp[i][j] = 1;
        }
    }

    for(int i = 3; i <= 10000; i++) {
        for(int j = 2; j <= 100; j++) {
            if(i > j) {
                dp[i][j] = (dp[i-j][j] + dp[i-1][j]) % MOD;
            }
        }
    }

    cout << dp[N][M] % MOD;
}

void input() {
    cin >> N >> M;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
