#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define Endl "\n"
#define MAX 1e9

struct turninfo {
    int r, c, s;
};

int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M, K;
int graph[51][51];
int Map[51][51];        // 복사본
vector<turninfo> v;
bool visited[7];
int order[7];
int result = MAX;

void rotate(int r, int c, int s) {
    for(int i = 1; i <= s; i++) {
        int tmp = Map[r-i][c-i];

        // 왼쪽 변
        for(int j = r - i + 1; j <= r + i; j++) {
            Map[j-1][c-i] = Map[j][c-i];
        }

        // 아래쪽 변
        for(int j = c - i + 1; j <= c + i; j++) {
            Map[r+i][j-1] = Map[r+i][j];
        }

        // 오른쪽 변
        for(int j = r + i - 1; j >= r - i; j--) {
            Map[j+1][c + i] = Map[j][c + i];
        }

        for(int j = c + i - 1; j > c - i; j--) {
            Map[r-i][j + 1] = Map[r - i][j];
        }
        Map[r - i][c - i + 1] = tmp;
    }
}

void simulation() {
    int res = 0;
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
            Map[i][j] = graph[i][j];
        }
    }

    for(int i = 0; i < K; i++) {
        int od = order[i];
        int r = v[od].r;
        int c = v[od].c;
        int s = v[od].s;
        rotate(r, c, s);
    }

    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
            res += Map[i][j];
        }
        result = min(result, res);
        res = 0;
    }
}

void dfs(int x) {
    if(x == K) {
        simulation();
        return;
    }

    for(int i = 0; i < K; i++) {
        if(!visited[i]) {
            visited[i] = true;
            order[x] = i;
            dfs(x+1);
            visited[i] = false;
        }
    }
}


void solve() {
    dfs(0);

    cout << result;
}

void input() {
    cin >> N >> M >> K;

    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
            cin >> graph[i][j];
        }
    }
    for(int i = 0; i < K; i++) {
        int r, c, s;
        cin >> r >> c >> s;
        v.push_back({r, c, s});
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

