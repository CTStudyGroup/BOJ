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

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int N, M, K;
int arr[1025][1025];
int dp[1025][1025];

void Print() {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
}

void solve() {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + arr[i][j] - dp[i-1][j-1];
        }
    }
}

void input() {
    cin >> N >> M;

    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
            cin >> arr[i][j];
        }
    }

    solve();
    cin >> K;

    for(int i = 0; i < K; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        cout << dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1] << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
