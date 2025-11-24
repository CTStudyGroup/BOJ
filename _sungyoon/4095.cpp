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
int N, M;
int graph[1001][1001];
int dp[1001][1001];

void Print() {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
            cout << dp[i][j] <<  " ";
        }
        cout << endl;
    }
}

void solve() {
    int answer = 0;

    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
            if(graph[i][j] == 1) {
                dp[i][j] = min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]}) + 1;
                answer = max(answer, dp[i][j]);
            }
        }
    }

    cout << answer << endl;
}

void input() {
    while(true) {
        cin >> N >> M;

        memset(dp, 0, sizeof(dp));

        if(N == 0 && M == 0) exit(0);

        for(int i = 1; i <= N; i++) {
            for(int j = 1; j <= M; j++) {
                cin >> graph[i][j];
            }
        }

        solve();
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}

