#include <iostream>
#include <vector>

using namespace std;

int recursive(vector<int> &dp, vector<vector<int>>& create_times, int idx) {
	if (dp[idx] != -1)
		return dp[idx];

	int time = 0;
	for (int i = 1; i < create_times[idx].size(); i++) {
		int cur = recursive(dp, create_times, create_times[idx][i]);
		time = max(time, cur);
	}
	dp[idx] = time + create_times[idx][0];
	return dp[idx];
}

int main() {
	int N;
	cin >> N;

	vector<vector<int>> create_times(N);
	for (int i = 0; i < N; i++) {
		int cur;
		cin >> cur;
		create_times[i].push_back(cur);

		while (1) {
			cin >> cur;

			if (cur == -1)
				break;
			create_times[i].push_back(--cur);
		} 
	}

	vector<int> dp(N, -1);
	for (int i = 0; i < N; i++)
		cout << recursive(dp, create_times, i) << "\n";

	return 0;
}