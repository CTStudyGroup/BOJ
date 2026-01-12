#include <bits/stdc++.h>
#include <stdio.h> // scanf 사용을 위해 추가

using namespace std;

int direction[4][2] = { {-1,0}, {0,-1}, {1, 0}, {0, 1} };
const int MAX = 52;
int maximum = -1;

int arr[MAX][MAX];
queue<pair<int, int>> que;
int n, m, ans;

bool IsInside(int x, int y) {
    return x >= 0 && x <= n + 1 && y >= 0 && y <= m + 1;
}

void bfs(int height) {
    arr[0][0] = height;
    que.push({ 0, 0 });

    bool visited[MAX][MAX] = { false, };
    visited[0][0] = true;

    while (!que.empty())
    {
        int CurX = que.front().first;
        int CurY = que.front().second;
        que.pop();

        for (auto& dir : direction) {
            int nextX = CurX + dir[0];
            int nextY = CurY + dir[1];

            if (IsInside(nextX, nextY) && arr[nextX][nextY] < height) {
                arr[nextX][nextY] = height;  
                que.push({ nextX, nextY });
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            scanf_s("%1d", &arr[i][j]);
            maximum = max(maximum, arr[i][j]);
        }
    }

    for (int k = 1; k <= maximum; k++) {
        bfs(k);

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (arr[i][j] < k) {
                    ans += 1;
                    arr[i][j] += 1;
                }
            }
        }
    }

    cout << ans << endl;

    return 0;
}