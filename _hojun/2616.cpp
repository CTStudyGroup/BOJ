#include <bits/stdc++.h>

using namespace std;

int main() {
	int n, k; 
	cin >> n;
	
	vector<int> arr(n + 1);
	vector<vector<int>> dp(4, vector<int>(n + 1, 0));

	for (int i = 1; i <= n; ++i) {
		int tmp;
		cin >> tmp;
		arr[i] = tmp + arr[i - 1];
	}

	cin >> k;

	for (int i = 1; i < 4; ++i) {
		for (int j = i * k; j <= n; ++j) {
			dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - k] + (arr[j] - arr[j - k]));
		}
	}

	cout << dp[3][n];

	return 0;
}