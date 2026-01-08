#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int dy[4] = { 1, -1, 0, 0 };
int dx[4] = { 0, 0, 1, -1 };
void BFS(vector<vector<int>> &board, int h) {
    vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size(), false));
    queue<pair<int, int>> q;

    q.push({ 0, 0 });
    visited[0][0] = true;
    board[0][0] = h;
    while (!q.empty()) {
        pair<int, int> front = q.front();
        q.pop();

        for (int dir = 0; dir < 4; dir++) {
            int ny = front.first + dy[dir];
            int nx = front.second + dx[dir];

            if (ny < 0 || nx < 0 || ny >= board.size() || nx >= board[0].size() || visited[ny][nx])
                continue;
            visited[ny][nx] = true;

            if (board[ny][nx] < h) {
                q.push({ ny, nx });
                board[ny][nx] = h;
            }
        }
    }
}

void print(vector<vector<int>> &board) {
    for (int y = 0; y < board.size(); y++) {
        for (int x = 0; x < board[0].size(); x++) {
            cout << board[y][x] << " ";
        }
        cout << "\n";
    }
    cout << "\n";
}

int main() {
    int N, M;
    cin >> N >> M;

    int maxV = 0;
    vector<vector<int>> board(N + 2, vector<int>(M + 2));
    for (int y = 1; y <= N; y++) {
        string input;
        cin >> input;
        for (int x = 0; x < M; x++) {
            board[y][x + 1] = input[x] - '0';
            maxV = max(maxV, board[y][x + 1]);
        }
    }
    // print(board);

    int answer = 0;
    for (int h = 1; h <= maxV; h++) {
        BFS(board, h);
        // print(board);

        for (int y = 1; y <= N; y++) {
            for (int x = 1; x <= M; x++) {
                if (board[y][x] < h) {
                    answer += 1;
                    board[y][x] = h;
                }
            }
        }
    }

    cout << answer;

    return 0;
}
