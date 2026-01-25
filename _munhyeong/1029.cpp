#include <iostream>
#include <vector>

using namespace std;

int recursive(vector<vector<int>> &price, vector<vector<vector<int>>> &dp, int visited, int artist, int boundary) {
	int& ret = dp[visited][artist][boundary];
	if (ret != -1)
		return ret;

	ret = 0;
	for (int i = 1; i < price.size(); i++) {
		if (!(visited & (1 << i)) && price[artist][i] >= boundary) {
			int next_visited = visited | (1 << i);
			ret = max(ret, recursive(price, dp, next_visited, i, price[artist][i]) + 1);
		}
	}

	return ret;
}

int main() {
	int N;
	cin >> N;

	vector<vector<int>> price(N, vector<int>(N));
	for (int i = 0; i < N; i++) {
		string input;
		cin >> input;

		for (int x = 0; x < N; x++)
			price[i][x] = input[x] - '0';
	}

	vector<vector<vector<int>>> dp(1 << N, vector<vector<int>>(N, vector<int>(10, -1)));
	recursive(price, dp, 1, 0, 0);

	cout << dp[1][0][0] + 1;

	return 0;
}
