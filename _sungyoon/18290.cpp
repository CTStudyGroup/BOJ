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

int dx[] = {0, 0, -1, 1, 1, -1, -1, 1};
int dy[] = {-1, 1, 0, 0, -1, 1, -1, 1};
int N, M, K;
int graph[11][11];
int visited[11][11];
int result = -MAX;

bool ischeck(int x, int y) {
    return x >= 0 && x < N && y >= 0 && y < M;
}

void bt(int idx, int cnt) {
    if(idx == K) {
        result = max(result, cnt);
        return;
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(visited[i][j] == 0) {
                visited[i][j]++;
                if(ischeck(i+1, j)) {
                    visited[i+1][j]++;
                }
                if(ischeck(i, j+1)) {
                    visited[i][j+1]++;
                }
                if(ischeck(i-1, j)) {
                    visited[i-1][j]++;
                }
                if(ischeck(i, j-1)) {
                    visited[i][j-1]++;
                }
                bt(idx+1, cnt + graph[i][j]);
                visited[i][j]--;
                if(ischeck(i-1, j)) visited[i-1][j]--;
                if(ischeck(i+1, j)) visited[i+1][j]--;
                if(ischeck(i, j-1)) visited[i][j-1]--;
                if(ischeck(i, j+1)) visited[i][j+1]--;
            }
        }
    }
}

void solve() {
    bt(0, 0);

    cout << result;
}

void input() {
    cin >> N >> M >> K;

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
