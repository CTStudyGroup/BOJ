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
int N, K;
ll result;
int arr[1000001];

void solve() {
    K = K * 2 + 1;

    ll res = 0;

    for(int i = 0; i < 1000001; i++) {
        if(i >= K) res -= arr[i-K];
        res += arr[i];
        result = max(result, res);
    }

    cout << result;
}

void input() {
    cin >> N >> K;

    for(int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        arr[b] = a;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
