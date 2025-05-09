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
int N, M;
vector<vector<int>> v(2001);
bool visited[2001];

void dfs(int start, int depth) {
    if(depth == 4) {
        cout << 1;
        exit(0);
    }

    visited[start] = true;

    for(auto &it : v[start]){
        if(!visited[it]) {
            dfs(it, depth+1);
        }
    }

    visited[start] = false;
}

void solve() {
    for(int i = 0; i < N; i++) {
        memset(visited, 0, sizeof(visited));
        dfs(i, 0);
    }

    cout << 0;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
