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
ll N, P, Q, X, Y;
unordered_map<ll, ll> um;

ll solve(ll n) {
    ll ret;

    if(um.find(n) != um.end()) {
        return um[n];
    }

    ret = solve(n / P - X > 0? n / P - X : 0) + solve(n / Q - Y > 0? n / Q - Y : 0);
    um[n] = ret;
    return ret;
}

void input() {
    cin >> N >> P >> Q >> X >> Y;
    um[0] = 1;

    if(N == 0) {
        cout << 1;
        return;
    }

    cout << solve(N);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
