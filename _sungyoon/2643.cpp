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
int N, result;
vector<pii> v;
int dp[1001];

void solve() {
    sort(v.begin(), v.end());
    fill(dp, dp + N, 1);

    for(int i = 0; i < N; i++) {

        for(int j = 0; j < i; j++) {
            if(v[i].first >= v[j].first && v[i].second >= v[j].second) {
                dp[i] = max(dp[i], dp[j]+1);
            }
        }
        result = max(dp[i], result);
    }

    cout << result;
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        int left = min(a, b);
        int right = max(a, b);
        v.push_back(make_pair(left, right));
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
