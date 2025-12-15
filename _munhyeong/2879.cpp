#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int answer = 0;
void recursive(vector<int> &needs, int left, int right) {
	bool is_minus = (needs[left] < 0);

	int max_v = -987654321;
	int min_v = 987654321;
	for (int i = left; i <= right; i++) {
		if (is_minus)
			max_v = max(needs[i], max_v);
		else
			min_v = min(needs[i], min_v);
	}

	int value;
	if (is_minus) {
		value = max_v;
		answer += -max_v;
	}
	else {
		value = min_v;
		answer += min_v;
	}

	for (int i = left; i <= right; i++) {
		needs[i] -= value;
		//cout << needs[i] << " ";
	}
	//cout << "\n";


	int end = right;
	while (left <= end) {
		while (left <= end && !needs[left])
			left++;
		
		if (left > end)
			break;

		int right = left;
		while (right + 1 <= end) {
			if (!needs[right + 1])
				break;
			right++;
		}
		recursive(needs, left, right);
	}
}

int main() {
	int N;
	cin >> N;

	vector<int> current(N);
	for (auto& e : current)
		cin >> e;

	vector<int> needs(N);
	for (int i = 0; i < N; i++) {
		int e;
		cin >> e;
		needs[i] = e - current[i];
	}

	//for (auto e : needs) {
	//	cout << e << " ";
	//}
	//cout << "\n";

	// 연속된 구간 찾기
	int left = 0;
	while (left < N) {
		while (left < N && !needs[left])
			left++;

		if (left >= N)
			break;

		int right = left;
		bool is_minus = needs[left] < 0;
		while (right + 1 < N) {
			if (!needs[right + 1])
				break;
			else if (is_minus && needs[right + 1] > 0)
				break;
			else if (!is_minus && needs[right + 1] < 0)
				break;
			right++;
		}
		//cout << left << " " << right << "\n";
		recursive(needs, left, right);

		left = right + 1;
	}

	//cout << "\n";
	cout << answer;


	return 0;
}
