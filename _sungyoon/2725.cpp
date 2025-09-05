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

struct Customer {
    int x;
    int y;
    int Dest_x;
    int Dest_y;
};

int dx[] = {-1, 0, 0, 1, 1, -1, -1, 1};
int dy[] = {0, -1, 1, 0, -1, 1, -1, 1};
//int dx[] = {0, -1, -1, 0, 1, 1, 1, 0, -1};
//int dy[] = {0,0, -1, -1, -1, 0, 1, 1, 1};
//int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
//int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
int C, N;
int dp[1001];

void solve() {
    dp[1] = 3;

    for(int i = 2; i <= 1000; i++) {
        int cnt = 0;
        for(int j = 1; j < i; j++) {
            if(gcd(i, j) == 1) {
                cnt++;
            }
        }
        dp[i] = dp[i-1] + cnt * 2;
    }
}

void input() {
    cin >> C;

    solve();

    while(C--) {
        cin >> N;

        cout << dp[N] << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
