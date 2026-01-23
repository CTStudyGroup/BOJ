#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
	int N, M;
	cin >> N >> M;

	vector<vector<long long>> board(N, vector<long long>(M));
	vector<vector<long long>> sum_board(N, vector<long long>(M));
	for (int y = 0; y < N; y++) {
		string input;
		cin >> input;

		for (int x = 0; x < M; x++) {
			board[y][x] = (long long)input[x] - '0';
		}
	}

	sum_board[0][0] = board[0][0];
	for (int x = 1; x < M; x++)
		sum_board[0][x] = sum_board[0][x - 1] + board[0][x];
	for (int y = 1; y < N; y++)
		sum_board[y][0] = sum_board[y - 1][0] + board[y][0];

	for (int y = 1; y < N; y++) {
		for (int x = 1; x < M; x++) {
			sum_board[y][x] =
				sum_board[y - 1][x] +
				sum_board[y][x - 1] -
				sum_board[y - 1][x - 1] +
				board[y][x];

		}
	}

	// 0, 0을 포함하는 모든 직사각형을 구하기 
	long long A, B, C;
	long long answer = 0;
	for (int y = 0; y < N; y++) {
		for (int x = 0; x < M; x++) {
			long long A = sum_board[y][x];

			// 해당 직사각형을 기준으로 x가 같은 또 다른 직사각형 
			// 즉, y + 1 ~ N - 1까지
			if (y != N - 1) {
				B = sum_board[N - 1][x] - A;
				C = sum_board[N - 1][M - 1] - A - B;

				answer = max(answer, A * B * C);
			}


			// 해당 직사각형을 기준으로 y가 같은 또 다른 직사각형
			// 즉, x + 1 ~ M - 1까지
			if (x != M - 1) {
				B = sum_board[y][M - 1] - A;
				C = sum_board[N - 1][M - 1] - A - B;

				answer = max(answer, A * B * C);
			}
		}
	}

	// 높이가 전부 같은
	for (int x = 0; x < M - 2; x++) {
		for (int xx = x + 1; xx < M - 1; xx++) {
			long long A = sum_board[N - 1][x];
			long long B = sum_board[N - 1][xx] - A;
			long long C = sum_board[N - 1][M - 1] - A - B;

			answer = max(answer, A * B * C);
		}
	}

	// 너비가 전부 같은
	for (int y = 0; y < N - 2; y++) {
		for (int yy = y + 1; yy < N - 1; yy++) {
			long long A = sum_board[y][M - 1];
			long long B = sum_board[yy][M - 1] - A;
			long long C = sum_board[N - 1][M - 1] - A - B;

			answer = max(answer, A * B * C);
		}
	}

	// 0, 0을 포함한 직사각형이 가로로 꽉 찬 사각형이라면?
	for (int y = 0; y < N - 2; y++) {
		long long A = sum_board[y][M - 1];
		for (int x = 0; x < M - 1; x++) {
			// 나머지 사각형은 나머지를 각각 가져가야 함
			long long B = sum_board[N - 1][x] - sum_board[y][x];
			long long C = sum_board[N - 1][M - 1] - A - B;

			answer = max(answer, A * B * C);
		}
	}


	// 0, 0을 포함한 직사각형이 세로로 꽉 찬 사각형이라면?
	for (int x = 0; x < M - 2; x++) {
		long long A = sum_board[N - 1][x];
		for (int y = 0; y < N - 1; y++) {
			// 나머지 사각형은 나머지를 각각 가져가야 함
			long long B = sum_board[y][M - 1] - sum_board[y][x];
			long long C = sum_board[N - 1][M - 1] - A - B;

			answer = max(answer, A * B * C);
		}
	}

	cout << answer;

	return 0;
}
