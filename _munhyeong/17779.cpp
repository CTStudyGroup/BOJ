#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int diff(vector<vector<int>> &board, int x, int y, int d1, int d2) {
	vector<int> constituency(5, 0);

	int N = board.size() - 1;
	for (int r = 1; r <= N; r++) {
		for (int c = 1; c <= N; c++) {
			if (r < x + d1 && c <= y && !(r >= x && c >= y - (r - x))) {
				constituency[0] += board[r][c];
			}
			else if (r <= x + d2 && c > y && !(r >= x && c <= y + (r - x))) {
				constituency[1] += board[r][c];
			}
			else if (r >= x + d1 && c < y - d1 + d2 && !(r <= x + d1 + d2 && c >= (y - d1 + d2 - (x + d1 + d2 - r)))) {
				constituency[2] += board[r][c];
			}
			else if (r > x + d2 && c >= y - d1 + d2 && !(r <= x + d1 + d2 && c <= (y - d1 + d2 + (x + d1 + d2 - r)))) {
				constituency[3] += board[r][c];
			}
			else {
				constituency[4] += board[r][c];
			}
		}
	}

	int max_v = *max_element(constituency.begin(), constituency.end());
	int min_v = *min_element(constituency.begin(), constituency.end());

	return max_v - min_v;
}

int process(vector<vector<int>> &board) {
	int res = 987654321;

	int N = board.size() - 1;
	for (int x = 1; x <= N - 2; x++) {
		for (int y = 2; y <= N - 1; y++) {
			for (int d1 = 1; d1 <= y - 1 && d1 <= N - x - 1; d1++) {
				for (int d2 = 1; d2 <= N - y && d2 <= N - x - 1; d2++) {
					res = min(res, diff(board, x, y, d1, d2));
				}
			}
		}
	}

	return res;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int N;
	cin >> N;
	vector<vector<int>> board(N + 1, vector<int>(N + 1));

	for (int x = 1; x <= N; x++) {
		for (int y = 1; y <= N; y++) {
			cin >> board[x][y];
		}
	}

	cout << process(board) << endl;

	return 0;
}