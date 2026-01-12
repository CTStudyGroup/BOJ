#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int recursive(vector<int>& arr, vector<vector<int>>& dp, int s, int e) {
	if (s >= e) return 0;
	if (dp[s][e]) return dp[s][e];

	if (arr[s] == arr[e])
		return recursive(arr, dp, s + 1, e - 1);

	return dp[s][e] = min(recursive(arr, dp, s + 1, e) + 1, recursive(arr, dp, s, e - 1) + 1);
}

int main() {
	int N;
	cin >> N;

	vector<int> arr(N);
	for (auto& e : arr)
		cin >> e;

	vector<vector<int>> dp(N, vector<int>(N));
	cout << recursive(arr, dp, 0, N - 1);

	return 0;
}
