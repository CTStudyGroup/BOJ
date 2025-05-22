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
int N;
ll dp[1000001];

void solve() {
    dp[0] = 0;
    dp[1] = 1;

    for(int i = 2; i < 1000001; i++) {
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000000;
    }

    if(N < 0) {
        if(abs(N) % 2 == 0) {
            cout << -1 << endl << dp[abs(N)];
        }
        else cout << 1 << endl << dp[abs(N)];
    }
    else if(N == 0) cout << 0 << endl << dp[0];
    else cout << 1 << endl << dp[N];
}

void input() {
    cin >> N;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
