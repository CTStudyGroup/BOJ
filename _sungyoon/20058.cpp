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

int dx[] = {0, -1, 0, 1, 1, -1, -1, 1};
int dy[] = {-1, 0, 1, 0, -1, 1, -1, 1};
int N, Q;
int graph[65][65];
bool visited[65][65];
int tmp_graph[65][65];
int arr[1001];
int answer, result;

int bfs(int a, int b) {
    queue<pii> q;
    q.push({a, b});
    visited[a][b] = true;
    int cnt = 1;

    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx >= 0 && nx < N && ny >= 0 && ny < N) {
                if(graph[nx][ny] != 0 && !visited[nx][ny]) {
                    q.push({nx, ny});
                    visited[nx][ny] = true;
                    cnt++;
                }
            }
        }
    }
    return cnt;
}

void calculate() {
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            if(graph[i][j] == 0) continue;
            if(visited[i][j]) continue;

            int Size = bfs(i, j);
            result = max(result, Size);
        }
    }
}

void Copy() {
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            tmp_graph[i][j] = graph[i][j];
        }
    }
}

void redo() {
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            graph[i][j] = tmp_graph[i][j];
        }
    }
}

void melt() {
    vector<pii> v;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            if(graph[i][j] == 0) continue;

            int cnt = 0;
            for(int k = 0; k < 4; k++) {
                int nx = i + dx[k];
                int ny = j + dy[k];

                if(nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

                if(graph[nx][ny] == 0) continue;

                cnt++;
            }
            if(cnt < 3) v.push_back({i, j});
        }
    }

    for(auto it : v) {
        int x = it.first;
        int y = it.second;

        graph[x][y]--;
        answer--;
    }
}

void rotate(int x, int y, int lens) {
    for(int i = 0; i < lens; i++) {
        for(int j = 0; j < lens; j++) {
            tmp_graph[x+j][y + lens -1 - i] = graph[x + i][y + j];
        }
    }
}

void remake(int lens) {
    Copy();
    for(int i = 0; i < N; i += lens) {
        for(int j = 0; j < N; j += lens) {
            rotate(i, j, lens);
        }
    }
    redo();
}

void solve() {
    for(int i = 0; i < Q; i++) {
        int lens = (1 << arr[i]);
        remake(lens);
        melt();
    }
    calculate();

    cout << answer << endl << result;
}

void input() {
    cin >> N >> Q;

    N = (1 << N);

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> graph[i][j];
            answer += graph[i][j];
        }
    }

    for(int i = 0; i < Q; i++) {
        cin >> arr[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
