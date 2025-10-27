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

struct halloween {
    int cnt;
    int score;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int N;
int dp[5][32769];

void solve() {
    dp[0][0] = 1;

    for(int j = 1; j <= 32768; j++) {
        for(int i = 1; i < 5; i++) {
            for(int k = j * j; k <= 32768; k++) {
                dp[i][k] += dp[i-1][k - j * j];
            }
        }
    }
}

void input() {
    solve();

    while(true) {
        cin >> N;

        if(N == 0) return;

        int answer = 0;

        for(int i = 1; i <= 4; i++) {
            answer += dp[i][N];
        }
        
        cout << answer << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}

