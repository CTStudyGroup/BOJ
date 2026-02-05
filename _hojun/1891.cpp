#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int n;
int arr[5001];
int dp[5001][5001];

int pal(int s, int e) {
	if (s >= e) return 0; // 종료조건

	if (dp[s][e] != -1) return dp[s][e];

	int cnt = 0;
	if (arr[s] == arr[e]) {
		cnt = pal(s + 1, e - 1);
	}

	else {
		// s앞에 arr[e] 값 추가, e뒤에 arr[s] 값 추가
		cnt = min(pal(s, e - 1) + 1, pal(s + 1, e) + 1);
	}

	return dp[s][e] = cnt;
}


int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			dp[i][j] = -1;
		}
	}

	cout << pal(0, n - 1);

	return 0;
}
