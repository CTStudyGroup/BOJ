#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {-1 ,1, 0, 0};
int dy[] = {0, 0, -1, 1};
int N;
int graph[65][65];
bool visited[65][65];
bool success;

void dfs(int x, int y) {
    if(x >= 0 && y >= 0 && x < N && y < N) {
        if(!visited[x][y]) {
            visited[x][y] = true;
            int jump = graph[x][y];

            dfs(x+jump, y);
            dfs(x, y+jump);
        }
    }
}

void solve() {
    dfs(0, 0);

    if(visited[N-1][N-1]) cout << "HaruHaru";
    else cout << "Hing";
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> graph[i][j];
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
