#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define Endl "\n"
#define MAX 1e9

int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M;
int result = 0;
int graph[51][51];

void bfs(int x, int y) {
    bool visited[51][51];
    memset(visited, 0, sizeof(visited));
    queue<tuple<int, int, int>> q;
    q.push(make_tuple(x, y, 0));

    while(!q.empty()) {
        int xx = get<0>(q.front());
        int yy = get<1>(q.front());
        int zz = get<2>(q.front());
        q.pop();

        for(int i = 0; i < 8; i++) {
            int nx = xx + dx[i];
            int ny = yy + dy[i];

            if(nx >= 0 && nx < N && ny >= 0 && ny < M) {
                if(!visited[nx][ny]) {
                    if(graph[nx][ny] == 0) {
                        q.push(make_tuple(nx, ny, zz+1));
                        visited[nx][ny] = true;
                    }
                    else {
                        result = max(result, zz+1);
                        return;
                    }
                }
            }
        }
    }
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cin >> graph[i][j];
        }
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(graph[i][j] == 0) {
                bfs(i, j);
            }
        }
    }

    cout << result;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}

