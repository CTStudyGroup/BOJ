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

//int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
//int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
int T, N;
int MOD = 1000000007;
priority_queue<ll, vector<ll>, greater<ll>> pq;

void solve() {
    ll result = 1;
    while(pq.size() > 1) {
        ll a = pq.top();
        pq.pop();
        ll b = pq.top();
        pq.pop();

        result *= (a % MOD) * (b % MOD) % MOD;
        pq.push(a * b);
        result %= MOD;
    }

    cout << result % MOD << endl;
    pq.pop();
}

void input() {
    cin >> T;

    while(T--) {
        cin >> N;

        for(int i = 0; i < N; i++) {
            ll a;
            cin >> a;
            pq.push(a);
        }

        solve();
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
