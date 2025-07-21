#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int N, T, result;
int weight[101];
int value[101];
int dp[101][10001];

void solve() {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= T; j++) {
            if(weight[i] > j) {
                dp[i][j] = dp[i-1][j];
                result = max(result, dp[i][j]);
            }
            else {
                dp[i][j] = max(dp[i-1][j], value[i] + dp[i-1][j-weight[i]]);
                result = max(result, dp[i][j]);
            }
        }
    }

    cout << result;
}

void input() {
    cin >> N >> T;

    for(int i = 1; i <= N; i++) {
        int a, b;
        cin >> a >> b;
        weight[i] = a;
        value[i] = b;
    }

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
