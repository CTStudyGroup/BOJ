#include <iostream>
#include <vector>
#include <deque>

using namespace std;

struct Info {
	int cnt;
	int y;
	int x;
};

int visited[51][51] = { 0, };

int dy[4] = { 1, -1, 0, 0 };
int dx[4] = { 0, 0, 1, -1 };
int dfs(vector<string>& board, int& r, int& c, int y, int x) {
	int &ret = visited[y][x];
	if (ret) return ret;
	ret = -1;

	int step = 1;
	int move = board[y][x] - '0';
	for (int dir = 0; dir < 4; dir++) {
		int ny = y + (move * dy[dir]);
		int nx = x + (move * dx[dir]);

		if (ny < 0 || nx < 0 || ny >= r || nx >= c)
			continue;

		if (board[ny][nx] == 'H')
			continue;

		// visited 검사
		int cur = dfs(board, r, c, ny, nx);
		if (cur == -1)
			return -1;
		step = max(step, cur + 1);
	}

	return ret = step;
}

int main() {
	int r, c;
	cin >> r >> c;

	vector<string> board(r);
	for (int y = 0; y < r; y++)
		cin >> board[y];

	cout << dfs(board, r, c, 0, 0) << "\n";

	/*
	for (int y = 0; y < r; y++) {
		for (int x = 0; x < c; x++) {
			cout << visited[y][x] << " ";
		}
		cout << "\n";
	}
	*/

	return 0;
}
