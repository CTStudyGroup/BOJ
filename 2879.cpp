#include <bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N; cin >> N;
	vector<int> arr(N + 1, 0);

	for (int i = 0; i < N; i++)
		cin >> arr[i];

	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;

		arr[i] -= num;
	}

	int ans = 0;
	bool bIsChecked = true;

	while (bIsChecked)
	{
		bIsChecked = false;
		for (int i = 0; i < N; i++) {
			if (arr[i] == 0) continue;
			bIsChecked = true;
			int minValue = arr[i];

			for (int j = i + 1; j <= N; j++) {
				if (arr[i] * arr[j] > 0) {
					minValue = abs(arr[j]) < abs(arr[i]) ? arr[j] : arr[i];
				}
				else {
					ans += abs(minValue);
					for (int k = i;k < j;k++) arr[k] -= minValue;
					i = j - 1;
					break;
				}
			}
		}
	}
	cout << ans << " ";

	return 0;
}