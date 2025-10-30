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
int n;
int graph[2223][2223];
int dp[2223][2223];

void Print() {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
}

void solve() {
    dp[0][0] = 0;

    for(int i = 1; i < n; i++) {
        if(graph[i-1][0] > graph[i][0]) {
            dp[i][0] = dp[i-1][0];
        }
        else {
            dp[i][0] = dp[i-1][0] + (graph[i][0] - graph[i-1][0]) + 1;
        }
    }

    for(int j = 1; j < n; j++) {
        if(graph[0][j-1] > graph[0][j]) {
            dp[0][j] = dp[0][j-1];
        }
        else {
            dp[0][j] = dp[0][j-1] + (graph[0][j] - graph[0][j-1]) + 1;
        }
    }

    for(int i = 1; i < n; i++) {
        for(int j = 1; j < n; j++) {
            if(graph[i-1][j] > graph[i][j]) {
                dp[i][j] = min(dp[i-1][j], dp[i][j]);
            }
            else {
                dp[i][j] = min(dp[i][j], (graph[i][j] - graph[i-1][j] + 1) + dp[i-1][j]);
            }

            if(graph[i][j-1] > graph[i][j]) {
                dp[i][j] = min(dp[i][j-1], dp[i][j]);
            }
            else {
                dp[i][j] = min(dp[i][j], (graph[i][j] - graph[i][j-1] + 1) + dp[i][j-1]);
            }
        }
    }

    cout << dp[n-1][n-1];
}

void input() {
    cin >> n;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> graph[i][j];
            dp[i][j] = MAX;
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

