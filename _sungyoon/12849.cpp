#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

int dx[] = {-1, 0, 1, 0, 1, -1, -1, 1};
int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
int D;
vector<vector<int>> v(8);
vector<pii> tmp = {{0, 1}, {0, 2}, {1, 2}, {1, 3}, {2, 3}, {2, 4},
                   {3, 4}, {3, 5}, {4, 5}, {5, 6}, {6, 7}, {4, 7}};
ll dp[100001][8];

void solve() {
    for(auto it : tmp) {
        int a = it.first;
        int b = it.second;

        v[a].push_back(b);
        v[b].push_back(a);
    }

    dp[0][0] = 1;

    for(int i = 1; i <= 100000; i++) {
        for(int j = 0; j < 8; j++) {
            for(auto it : v[j]) {
                dp[i][it] += dp[i-1][j];
                dp[i][it] %= 1000000007;
            }
        }
    }

    cout << dp[D][0];
}

void input() {
    cin >> D;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
