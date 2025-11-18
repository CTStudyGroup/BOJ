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
// int dx[] = {0, 0, 1, -1};
// int dy[] = {1, -1, 0, 0};
int dx[] = {0, -1};
int dy[] = {-1, 0};
int N;
int graph[1002][1002];
int dp[1002][1002][3];      // 0: 딸기, 1 : 초코, 2 : 바나나

void solve() {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            for(int k = 0; k < 3; k++) {
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k]);
                dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k]);
            }

            if(graph[i][j] == 0) {
                dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][2] + 1);
                dp[i][j][0] = max(dp[i][j][0], dp[i][j-1][2] + 1);
            }

            if(graph[i][j] == 1) {
                if(dp[i-1][j][0] != 0) dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][0] + 1);
                if(dp[i][j-1][0] != 0) dp[i][j][1] = max(dp[i][j][1], dp[i][j-1][0] + 1);
            }

            if(graph[i][j] == 2)  {
                if(dp[i-1][j][1] != 0) dp[i][j][2] = max(dp[i][j][2], dp[i-1][j][1] + 1);
                if(dp[i][j-1][1] != 0) dp[i][j][2] = max(dp[i][j][2], dp[i][j-1][1] + 1);
            }
        }
    }

    int answer = 0;
    for(int i = 0; i < 3; i++) {
        answer = max(answer, dp[N][N][i]);
    }

    cout << answer;
}

void input() {
    cin >> N;

    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            cin >> graph[i][j];
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

