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
int N, result;
int arr[101];
int dp[101];
vector<pii> v;

void solve() {
    sort(v.begin(), v.end());

    for(int i = 0; i < N; i++) {
        arr[i] = v[i].second;
    }
    fill(dp, dp+N, 1);

    for(int i = 1; i < N; i++) {
        for(int j = i-1; j >= 0; j--) {
            if(arr[j] < arr[i]) {
                dp[i] = max(dp[i], dp[j]+1);
                result = max(result, dp[i]);
            }
        }
    }

    cout << N - result;
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        v.push_back({a, b});
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
