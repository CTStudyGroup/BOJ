#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

struct Tree {
    int Node, left, right;
};

const int INF = 1e9;
const int MAX = 1001;
const int MOD = 1e9 + 7;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int T, N, M;
int dp[MAX];

int func(int node, int par, vector<vector<pii>> &v) {
    int &ret = dp[node];

    if(ret != -1) return ret;

    ret = 0;

    bool isleaf = false;

    for(auto &it : v[node]) {
        int nextnode = it.first;
        int cost = it.second;

        if(par != nextnode) {
            isleaf = true;
            ret += min(func(nextnode, node, v), cost);
        }
    }

    return ((isleaf)? ret : INF);
}

void solve(vector<vector<pii>> &v) {
    if(N == 1) {
        cout << 0 << endl;
    }
    else cout << func(1, 0, v) << endl;
}

void input() {
    cin >> T;

    while(T--) {
        cin >> N >> M;

        vector<vector<pii>> v(N+1);

        memset(dp, -1, sizeof(dp));

        for(int i = 0; i < M; i++) {
            int a, b, c;
            cin >> a >> b >> c;
            v[a].push_back({b, c});
            v[b].push_back({a, c});
        }

        solve(v);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
