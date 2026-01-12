#include <bits/stdc++.h>

using namespace std;

int direction[4][2] = { {-1,0}, {0,-1}, {1, 0}, {0, 1} };
vector<vector<int>> Map;
vector<vector<int>> dp;
int n;

int GetDis(int y, int x) {
    int ret = 1;
    if (dp[y][x] != 0) return dp[y][x]; //값이 이미 있으면 바로 값을 반환합니다.

    dp[y][x] = 1;
    for (auto dir : direction) {
        int ny = dir[0] + y;
        int nx = dir[1] + x;

        if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
        if (Map[ny][nx] > Map[y][x]) { 
            dp[y][x] = max(dp[y][x], GetDis(ny, nx) + 1);
        }
    }
    return dp[y][x];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;

    Map.resize(n, vector<int>(n));
    dp.resize(n, vector<int>(n));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> Map[i][j];
        }
    }

    int maxDis = 1;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            maxDis = max(maxDis, GetDis(i, j));
        }
    }

    cout << maxDis << endl;
    return 0;
}