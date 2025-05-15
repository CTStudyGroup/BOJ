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
int N, result;
int arr[100001];
int dp[100001];

void solve() {
    for(int i = 1; i <= N; i++) {
        dp[i] = arr[i] + dp[i-1];
    }

    for(int i = 2; i < N; i++) {
        result = max(result, (dp[i] - arr[1]) + (dp[N-1] - dp[i-1]));       // 벌 꿀통 벌
        result = max(result, (dp[N] - dp[1] - arr[i]) + (dp[N] - dp[i]));      // 벌 벌 꿀통
        result = max(result, dp[i-1] + dp[N-1] - arr[i]);      // 꿀통 벌 벌
    }

    cout << result;
}

void input() {
    cin >> N;

    for(int i = 1; i <= N; i++) {
        cin >> arr[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
