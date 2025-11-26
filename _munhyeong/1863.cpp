#include <algorithm>
#include <iostream>
#include <deque>

using namespace std;

int main() {
	int n;
	int x, y;
	cin >> n;

	deque<int> dq;
	int answer = 0;
	for (int i = 0; i < n; i++) {
		cin >> x >> y;

		if (dq.empty() || dq.back() < y) {
			if (y == 0)
				continue;
			dq.push_back(y);
			answer++;
		}
		else {
			while (!dq.empty() && dq.back() > y) {
				dq.pop_back();
			}

			if (!dq.empty() && dq.back() == y)
				continue;

			if (y == 0)
				continue;
			answer++;
			dq.push_back(y);
		}
	}

	cout << answer;

	return 0;
}