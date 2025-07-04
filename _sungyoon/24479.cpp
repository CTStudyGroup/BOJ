#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    char map[5][7];
};

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M, R;
vector<vector<int>> v(100001);
int visited[100001];
int cnt = 1;

void dfs(int start) {
    visited[start] = cnt;

    for(int i = 0; i < v[start].size(); i++) {
        int nextNode = v[start][i];

        if(!visited[nextNode]) {
            cnt++;
            dfs(nextNode);
        }
    }
}

void solve() {
    dfs(R);

    for(int i = 1; i <= N; i++) {
        cout << visited[i] << "\n";
    }
}

void input() {
    cin >> N >> M >> R;

    for(int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    for(int i = 1; i <= N; i++) {
        sort(v[i].begin(), v[i].end());
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
