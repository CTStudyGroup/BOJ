#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

struct Tree {
    int Node, left, right;
};

const int INF = 1e9;
const int MAX = 101;
const int MOD = 1e9 + 7;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int n, m;
int graph[MAX][MAX];
int path[MAX][MAX];
vector<int> v;

void Print() {
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            if(graph[i][j] == INF) cout << 0 << " ";
            else cout << graph[i][j] << " ";
        }
        cout << endl;
    }
}

void find_route(int start, int end) {
    if(path[start][end] == 0) {
        v.push_back(start);
        v.push_back(end);
        return;
    }
    find_route(start, path[start][end]);
    v.pop_back();
    find_route(path[start][end], end);
}

void solve() {
    for(int k = 1; k <= n; k++) {
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                int value = graph[i][k] + graph[k][j];

                if(value < graph[i][j]) {
                    graph[i][j] = value;
                    path[i][j] = k;
                }
            }
        }
    }

    Print();
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            if(i == j || graph[i][j] == INF) cout << 0 << endl;
            else {
                v.clear();
                find_route(i, j);
                cout << v.size() << " ";
                for(auto &it : v) {
                    cout << it << " ";
                }
                cout << endl;
            }
        }
    }
}

void Init() {
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            if(i == j) continue;
            graph[i][j] = INF;
        }
    }
}

void input() {
    cin >> n >> m;

    Init();

    for(int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a][b] = min(graph[a][b], c);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
