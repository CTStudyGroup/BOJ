#include <bits/stdc++.h>
using namespace std;
#define INF 1e9
bool ladder[31][11];
int N, M, H;
int res = INF;

bool isValid() {
    for (int i = 1; i <= N; i++) {
        int curLine = i;
        for (int j = 1; j <= H; j++) {
            if (ladder[j][curLine])
                curLine++;
            else if (ladder[j][curLine - 1])
                curLine--;

        }
        if (curLine != i) return false;
    }
    return true;
}

void dfs(int index, int cnt) {
    if (cnt >= 4) {
        return;
    }
    if (isValid()) {
        res = min(res, cnt);
        return;
    }

    for (int i = index; i <= H; i++) {
        for (int j = 1; j <= N; j++) {
            if (ladder[i][j] || ladder[i][j - 1] || ladder[i][j + 1]) continue;
            ladder[i][j] = true;
            dfs(i, cnt + 1);
            ladder[i][j] = false;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M >> H;
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        ladder[a][b] = true;
    }

    dfs(1, 0);

    cout << ((res == INF) ? -1 : res) << "\n";

    return 0;
}