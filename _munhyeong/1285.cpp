#include <iostream>
#include <vector>

using namespace std;

void flip(vector<int>& coins, int idx) {
	coins[idx] = ~coins[idx];
}

int answer = 20 * 20 + 1;
void check_tails(vector<int> coins) {
	int sum = 0;
	int N = coins.size();
	// 0, 1, 2, 4
	for (int x = 1; x < (1 << N); x *= 2) {
		int cur_cnt = 0;
		for (int y = 0; y < N; y++) {
			if (coins[y] & x)
				cur_cnt++;
		}
		sum += min(cur_cnt, N - cur_cnt);
	}

	// cout << sum << "\n";
	answer = min(answer, sum);
}

void recursive(vector<int> coins, int idx) {
	if (idx >= coins.size()) {
		check_tails(coins);
		return;
	}

	recursive(coins, idx + 1);

	flip(coins, idx);
	recursive(coins, idx + 1);
}

int main() {
	int N;
	cin >> N;

	vector<int> coins(N, 0);
	for (int i = 0; i < N; i++) {
		string input;
		cin >> input;

		for (auto c : input) {
			coins[i] <<= 1;
			if (c == 'T') coins[i] += 1;
		}
	}
	
	recursive(coins, 0);

	cout << answer;

	return 0;
}