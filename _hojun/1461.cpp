#include <bits/stdc++.h>

using namespace std;

int main1461() {

	int N, M; cin >> N >> M;

	vector<int> arr(N);
	vector<int> arr1(N);
	vector<int> result;

	for (int i = 0; i < N; ++i) {
		int a; cin >> a;

		if (a > 0) arr[i] = a;
		else arr1[i] = -a;
	}

	sort(arr.begin(), arr.end(), greater<>());
	sort(arr1.begin(), arr1.end(), greater<>());

	for (int i = 0; i < arr.size(); i += M) {
		result.push_back(arr[i]);
	}
	for (int i = 0; i < arr1.size(); i += M) {
		result.push_back(arr1[i]);
	}

	int ans = 0;
	sort(result.begin(), result.end());

	for (int i = 0; i < result.size() - 1; ++i) {
		ans += result[i] * 2;
		cout << result[i] << "가 더해지면 ans 값" << ans << endl;
	}
	ans += result.back();

	cout << ans;

	return 0;
}