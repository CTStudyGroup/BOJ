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
int arr[9];
bool visited[9];
int dp[9];

int sum() {
    int res = 0;

    for(int i = 0; i < N - 1; i++) {
        res += abs(dp[i] - dp[i+1]);
    }

    return res;
}

void bt(int x) {
    if(x == N) {
        result = max(result, sum());
        return;
    }

    for(int i = 0; i < N; i++) {
        if(!visited[i]) {
            visited[i] = true;
            dp[x] = arr[i];
            bt(x+1);
            visited[i] = false;
        }
    }
}

void solve() {
    for(int i = 0; i < N - 1; i++) {
        result += abs(arr[i] - arr[i+1]);
    }

    bt(0);

    cout << result;
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
