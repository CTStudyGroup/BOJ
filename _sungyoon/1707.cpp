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

struct FISH {
    int x;
    int y;
    int Dir;
    bool live;
};

//int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
//int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int dx[] = {0, -1, -1, 0, 1, 1, 1, 0, -1};
int dy[] = {0,0, -1, -1, -1, 0, 1, 1, 1};
//int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
//int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};
int K, V, E;
vector<vector<int>> v(20001);
int visited[20001];
bool flag = true;

void dfs(int node, int visit) {
    visited[node] = visit;

    for(auto it : v[node]) {
        if(visited[it] == visit) {
            flag = false;
        }

        if(!visited[it]) {
            dfs(it, -visit);
        }
    }
}

void solve() {
    for(int i = 1; i <= V; i++) {
        if(!visited[i]) {
            dfs(i, 1);
        }
        if(!flag) break;
    }

    if(!flag) {
        cout << "NO" << endl;
    }
    else cout << "YES" << endl;
}

void input() {
    cin >> K;

    while(K--) {
        memset(visited, 0, sizeof(visited));
        flag = true;

        cin >> V >> E;

        for(int i = 0; i < E; i++) {
            int a, b;
            cin >> a >> b;
            v[a].push_back(b);
            v[b].push_back(a);
        }

        solve();
        for(int i = 1; i <= V; i++) {
            v[i].clear();
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
