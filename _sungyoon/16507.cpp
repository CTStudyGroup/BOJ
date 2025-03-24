#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int R, C, Q;
int graph[1001][1001];
int dp[1001][1001];

void accumulate() {
    for(int i = 1; i <= R; i++) {
        for(int j = 1; j <= C; j++) {
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + graph[i][j] - dp[i-1][j-1];
        }
    }
}

void input() {
    cin >> R >> C >> Q;

    for(int i = 1; i <= R; i++) {
        for(int j = 1; j <= C; j++) {
            cin >> graph[i][j];
        }
    }

    accumulate();

    for(int i = 0; i < Q; i++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        cout << (dp[c][d] - dp[c][b-1] - dp[a-1][d] + dp[a-1][b-1]) / ((c - a + 1) * (d - b + 1)) << endl;
    }
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}

