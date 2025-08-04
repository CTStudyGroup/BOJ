#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    string s;
    vector<int> v;
};

int dx[] = {-1, 0, 1, 0, 1, -1, -1, 1};
int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
ll K;

ll f(ll x) {
    if(x == 1) return 0;
    ll i;
    for(i = 1; i + i < x; i += i);
    return !f(x-i);
}

void solve() {
    cout << f(K);
}

void input() {
    cin >> K;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();

    return 0;
}
