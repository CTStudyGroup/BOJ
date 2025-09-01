#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    int y;
    int r;
};

int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M;
priority_queue<ll, vector<ll>, greater<ll>> pq;

void solve() {
    for(int i = 0; i < M; i++) {
        ll a = pq.top();
        pq.pop();
        ll b = pq.top();
        pq.pop();
        ll tmp = 0;
        tmp += a + b;
        pq.push(tmp);
        pq.push(tmp);
    }

    ll answer = 0;
    while(!pq.empty()) {
        answer += pq.top();
        pq.pop();
    }

    cout << answer;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        int a;
        cin >> a;
        pq.push(a);
    }
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

