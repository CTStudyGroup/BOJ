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

struct horse {
    int x;
    int y;
    int dir;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dx[] = {0, 0, 0, 1, -1};
int dy[] = {0, 1, -1, 0, 0};
int N;
vector<vector<int>> v(1000001);
int dp[1000001][2];

int dfs(int Node, int parent, int status) {
    if(dp[Node][status] != -1) return dp[Node][status];

    if(status == 1) {
        dp[Node][status] = 1;

        for(int i = 0; i < v[Node].size(); i++) {
            int nextNode = v[Node][i];

            if(parent != nextNode) {
                dp[Node][status] += min(dfs(nextNode, Node, 0), dfs(nextNode, Node, 1));
            }
        }
    }
    else {
        dp[Node][status] = 0;

        for(int i = 0; i < v[Node].size(); i++) {
            int nextNode = v[Node][i];

            if(parent != nextNode) {
                dp[Node][status] += dfs(nextNode, Node, 1);
            }
        }
    }

    return dp[Node][status];
}

void solve() {
    int res1 = dfs(1, -1, 0);
    int res2 = dfs(1, -1, 1);

    cout << min(res1, res2);
}

void input() {
    cin >> N;

    for(int i = 0; i < N-1; i++) {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    memset(dp, -1, sizeof(dp));
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

