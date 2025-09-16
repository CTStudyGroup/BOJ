#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M, K;
ll dp[101][101];
bool cango[201][201];

void solve() {
    for(int i = 1; i <= N; i++) {       // 가로
        if(cango[0][i*2-1]) break;
        dp[0][i] = 1;
    }

    for(int j = 1; j <= M; j++) {       // 세로
        if(cango[j*2-1][0]) break;
        dp[j][0] = 1;
    }

    for(int i = 1; i <= M; i++) {
        for(int j = 1; j <= N; j++) {
            if(cango[i*2-1][j*2] == 0) {
                dp[i][j] += dp[i-1][j];
            }
            if(cango[i*2][j*2-1] == 0) {
                dp[i][j] += dp[i][j-1];
            }
        }
    }

    cout << dp[M][N];
}

void input() {
    cin >> N >> M >> K;

    for(int i = 0; i < K; i++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;        // b, d(세로), a, c(가로)
        cango[b+d][a+c] = true;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
