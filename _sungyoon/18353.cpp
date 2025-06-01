#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e11

struct coordinate {
    int x;
    int y;
};

int dx[] = {0, 0, -1, 1, 1, -1, -1, 1};
int dy[] = {-1, 1, 0, 0, -1, 1, -1, 1};
int N, result;
int arr[2001];
int dp[2001];

void solve() {
    fill(dp, dp + N, 1);

    if(N == 1) {
        cout << 0;
        return;
    }

    for(int i = 1; i < N; i++) {
        for(int j = i-1; j >= 0; j--) {
            if(arr[j] > arr[i]) {
                dp[i] = max(dp[i], dp[j]+1);
            }
        }
    }

    for(int i = 0; i < N; i++) {
        result = max(result, dp[i]);
    }

    cout << N - result;
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        cin >> arr[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
