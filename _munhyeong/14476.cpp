#include <iostream>
#include <vector>

using namespace std;

int gcd(int a, int b) {
	return b ? gcd(b, a % b) : a;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N;
	cin >> N;

	vector<int> arr(N);
	for (auto& e : arr)
		cin >> e;

	vector<int> L2R(N);
	vector<int> R2L(N);

	L2R[0] = arr[0];
	R2L[N - 1] = arr[N - 1];

	for (int i = 1; i < N; i++) {
		L2R[i] = gcd(L2R[i - 1], arr[i]);
	}

	for (int i = N - 2; i >= 0; i--) {
		R2L[i] = gcd(R2L[i + 1], arr[i]);
	}

	int result = R2L[1];
	int num = arr[0];

	if (result < L2R[N - 2]) {
		num = arr[N - 1];
		result = L2R[N - 2];
	}

	for (int i = 1; i < N - 1; i++) {
		int val = gcd(L2R[i - 1], R2L[i + 1]);
		if (result < val) {
			result = val;
			num = arr[i];
		}
	}

	if (num % result) {
		cout << result << " " << num;
	}
	else {
		cout << -1;
	}

	return 0;
}
