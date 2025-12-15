#include <bits/stdc++.h>

using namespace std;

int calcMax(int a, int b, int c) {
	int res = max(a, b);
	return max(res, c);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int M, N; cin >> M >> N;
	vector<int> arr(2*M - 1, 1);

	for (int i = 0; i < N; ++i) {
		int a, b, c;
		cin >> a >> b >> c;

		int idx = 0;

		for (int j = 0; j < a; ++j) arr[idx++] += 0;
		for (int j = 0; j < b; ++j) arr[idx++] += 1;
		for (int j = 0; j < c; ++j) arr[idx++] += 2;
	}

	for (int i = M - 1; i >= 0; i--)
	{
		cout << arr[i] << ' ';
		for (int j = M; j < 2 * M - 1; j++)
			cout << arr[j] << ' ';
		cout << '\n';
	}


	return 0;
}