#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e8

struct coordinate {
    int x;
    int y;
};

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int T, K;
priority_queue<ll, vector<ll>, greater<ll>> pq;

void solve() {
    ll result = 0;

    while(pq.size() > 1) {
        ll a = pq.top();
        pq.pop();
        ll b = pq.top();
        pq.pop();
        result += a + b;
        pq.push(a + b);
    }

    cout << result << endl;
}

void input() {
    cin >> T;

    while(T--) {
        cin >> K;

        pq = {};

        for(int i = 0; i < K; i++) {
            int a;
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
