#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M;
int result;
int graph[101][71];
bool visited[101][71];

void bfs(int x, int y) {
    queue<pii> q;
    set<int> st;
    bool bong[101][71];
    memset(bong, 0, sizeof(bong));      // 같은 봉우리
    q.push(make_pair(x, y));
    visited[x][y] = true;
    bong[x][y] = true;

    while(!q.empty()) {
        int xx = q.front().first;
        int yy = q.front().second;
        q.pop();

        for(int i = 0; i < 8; i++) {
            int nx = xx + dx[i];
            int ny = yy + dy[i];

            if(nx >= 0 && ny >= 0 && nx < N && ny < M) {
                if(!bong[nx][ny] && graph[nx][ny] == graph[x][y]) {
                    q.push(make_pair(nx, ny));
                    visited[nx][ny] = true;
                    bong[nx][ny] = true;
                }
            }
        }
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(bong[i][j]) {
                for(int k = 0; k < 8; k++) {
                    int nx = i + dx[k];
                    int ny = j + dy[k];

                    if(nx >= 0 && ny >= 0 && nx < N && ny < M) {
                        st.insert(graph[nx][ny]);
                    }
                }
            }
        }
    }

    for(auto it : st) {
        if(graph[x][y] < it) {
            return;
        }
    }
    result++;
}

void solve() {
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(!visited[i][j] && graph[i][j] != 0) bfs(i, j);
        }
    }

    cout << result;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
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
