#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int N, M;
int arr[100001];
int dp[100001];

void accumulate() {
    for(int i = 1; i <= N; i++) {
        dp[i] = dp[i-1] + arr[i];
    }
}

void input() {
    cin >> N;

    for(int i = 1; i <= N; i++) {
        cin >> arr[i];
    }

    accumulate();

    cin >> M;

    for(int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        cout << dp[b] - dp[a] + arr[a] << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}

