#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"

struct Tree {
    int Node, left, right;
};

const int INF = 1e9;
const int MAX = 123457;
const int MOD = 1e9 + 7;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int N, M, maxheight;
int graph[51][51];

void bfs(int height) {
    graph[0][0] = height;
    queue<pii> q;
    q.push({0, 0});

    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx <= N+1 && nx >= 0 && ny <= M+1 && ny >= 0 && graph[nx][ny] < height) {
                graph[nx][ny] = height;
                q.push({nx, ny});
            }
        }
    }
}

void solve() {
    int answer = 0;

    for(int i = 1; i <= maxheight; i++) {
        bfs(i);

        for(int j = 1; j <= N; j++) {
            for(int k = 1; k <= M; k++) {
                if(graph[j][k] < i) {
                    answer++;
                    graph[j][k] += 1;
                }
            }
        }
    }

    cout << answer;
}

void input() {
    cin >> N >> M;

    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
            char a;
            cin >> a;
            graph[i][j] = a - '0';
            maxheight = max(maxheight, graph[i][j]);
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
