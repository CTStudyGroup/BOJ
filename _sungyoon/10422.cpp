#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

int dx[] = {-1, 0, 1, 0, 1, -1, -1, 1};
int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
int T, L;
ll dp[5001];

void solve() {
    dp[0] = 1;
    dp[2] = 1;

    for(int i = 2; i <= 2500; i++)  {
        for(int j = 0; j <= i-1; j++) {
            dp[i*2] += dp[j*2] * dp[(i-1-j)*2];
            dp[i*2] %= 1000000007;
        }
    }
}

void input() {
    cin >> T;

    solve();

    while(T--) {
        cin >> L;

        cout << dp[L] << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
