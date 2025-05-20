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
string s;
int arr[5001];
ll dp[5001];
int MOD = 1e6;

void solve() {
    if(s[0] == '0') {
        cout << 0;
        return;
    }

    dp[0] = 1;

    for(int i = 1; i <= s.size(); i++) {
        if(arr[i] >= 1 && arr[i] <= 9) {
            dp[i] = (dp[i - 1] + dp[i]) % MOD;
        }

        if(i == 0) continue;

        int stand = arr[i-1] * 10 + arr[i];

        if(10 <= stand && stand <= 26) {
            dp[i] = (dp[i-2] + dp[i]) % MOD;
        }
    }

    cout << dp[s.size()];
}

void input() {
    cin >> s;

    for(int i = 1; i <= s.size(); i++) {
        arr[i] = s[i-1] - '0';
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
