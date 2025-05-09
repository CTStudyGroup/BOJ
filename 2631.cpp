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
int N, maxv;
int arr[201];
int dp[201];

void solve() {
    fill(dp, dp+N, 1);

    for(int i = 2; i <= N; i++) {
        for(int j = 1; j < i; j++) {
            if(arr[j] < arr[i]) {
                dp[i] = max(dp[j]+1, dp[i]);
                maxv = max(dp[i], maxv);
            }
        }
    }
    
    cout << N - maxv;
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
