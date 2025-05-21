#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    int y;
};

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int T;
ll dp[100001][4];
int MOD = 1e9 + 9;

void solve() {
    dp[1][1] = 1;
    dp[2][2] = 1;
    dp[3][1] = dp[3][2] = dp[3][3] = 1;

    for(int i = 4; i <= 100000; i++) {
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD;
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD;
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD;
    }
}

void input() {
    cin >> T;

    solve();

    for(int i = 0; i < T; i++) {
        int a;
        cin >> a;
        cout << (dp[a][1] + dp[a][2] + dp[a][3]) % MOD << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
