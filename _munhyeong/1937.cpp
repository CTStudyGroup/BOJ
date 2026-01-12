#include <iostream>
#include <vector>

using namespace std;

int dy[4] = { 1, -1, 0, 0 };
int dx[4] = { 0, 0, 1, -1 };
int DFS(vector<vector<int>>& board, vector<vector<int>> &dp, int y, int x) {
    if (dp[y][x])
        return dp[y][x];
    dp[y][x] = 1; // 방문체크

    int maxV = 1;
    for (int dir = 0; dir < 4; dir++) {
        int ny = y + dy[dir];
        int nx = x + dx[dir];

        if (ny < 0 || nx < 0 || ny >= board.size() || nx >= board[0].size())
            continue;
        if (board[y][x] >= board[ny][nx])
            continue;

        maxV = max(maxV, DFS(board, dp, ny, nx) + 1);
    }

    return dp[y][x] = maxV;
}

void print(vector<vector<int>> dp) {
    int N = dp.size();
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < N; x++) {
            cout << dp[y][x] << " " ;
        }
        cout << endl;
    }
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    int N;
    cin >> N;

    vector<vector<int>> board(N, vector<int>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }

    vector<vector<int>> dp(N, vector<int>(N));
    int answer = 0;
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < N; x++) {
            answer = max(answer, DFS(board, dp, y, x));
            // print(dp);
            // cout << "\n";
        }
    }



    cout << answer;
}
