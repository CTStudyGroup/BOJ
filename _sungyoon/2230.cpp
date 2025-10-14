#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e10

struct coordinate {
    int x;
    int y;
    int r;
};

struct horse {
    int x;
    int y;
    int dir;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dx[] = {0, 0, 0, 1, -1};
int dy[] = {0, 1, -1, 0, 0};
int N, M;
vector<ll> v;

void solve() {
    sort(v.begin(), v.end());

    int le = 0;
    int ri = 0;
    ll diff = MAX;

    while(ri < N) {
        if(le == ri) {
            ri++;
            continue;
        }

        ll tmp = v[ri] - v[le];

        if(tmp >= M) {
            diff = min(tmp, diff);
            le++;
        }
        else ri++;
    }

    cout << diff;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        ll a;
        cin >> a;
        v.push_back(a);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

