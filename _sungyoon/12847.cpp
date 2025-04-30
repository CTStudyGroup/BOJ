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
int N, M;
int arr[100001];
int dp[100001];

void solve() {
    ll stand = 0;
    ll result = 0;

    for(int i = 0; i < M; i++) {
        stand += arr[i];
    }
    
    result = stand;

    for(int i = M; i < N; i++) {
        stand = stand - arr[i-M] + arr[i];
        result = max(result, stand);
    }

    cout << result;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        int a;
        cin >> arr[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
