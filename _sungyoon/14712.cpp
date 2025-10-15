#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

//int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
//int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dx[] = {0, -1, -1};
int dy[] = {-1, 0, -1};
int N, M, result;
int graph[26][26];

bool check(int x, int y) {
    int cnt = 0;

    for(int i = 0; i < 3; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx >= 0 && ny >= 0 && nx < N && ny < M) {
            if(graph[nx][ny] == 1) cnt++;
        }
    }

    if(cnt == 3) return false;
    return true;
}

void bt(int x, int y) {
    if(x == N-1 && y == M) {
        result++;
        return;
    }

    if(y == M) {
        y = 0;
        x++;
    }

    graph[x][y] = 1;
    if(check(x, y)) bt(x, y+1);
    graph[x][y] = 0;
    bt(x, y+1);
}

void solve() {
    bt(0, 0);

    cout << result;
}

void input() {
    cin >> N >> M;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
