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
int graph[33][33];
ll dp[3][33][33];

/*
 *       끝점에서 45도 회전하느냐, OR 그대로 직진하느냐   [0] = 오른쪽 [1] = 대각선 [2] = 아래
 */


void solve() {
    dp[0][0][1] = 1;

    for(int i = 2; i < N; i++) {        // 오른쪽 초기화
        if(graph[0][i] == 0) {
            dp[0][0][i] = dp[0][0][i-1];
        }
    }

    for(int i = 1; i < N; i++) {
        for(int j = 1; j < N; j++) {
            if(graph[i][j] == 0 && graph[i-1][j] == 0 && graph[i][j-1] == 0) {
                dp[1][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1];
            }

            if(graph[i][j] == 0) {
                dp[0][i][j] = dp[0][i][j-1] + dp[1][i][j-1];
                dp[2][i][j] = dp[2][i-1][j] + dp[1][i-1][j];
            }
        }
    }

    ll result = 0;

    for(int i = 0; i < 3; i++) {
        result += dp[i][N-1][N-1];
    }

    cout << result;
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
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
