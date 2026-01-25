#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
	int N;
	cin >> N;

	vector<int> rank;
	for (int i = 0; i < N; i++) {
		int input;
		cin >> input;

		rank.push_back(input);
	}

	int answer = 0;
	while (rank.size() != 1) {
		int max_v = 0;
		int max_i = -1;
		for (int i = 0; i < rank.size(); i++) {
			if (max_v < rank[i]) {
				max_i = i;
				max_v = rank[i];
			}
		}

		int cur_diff = 100000;
		if (0 < max_i)
			cur_diff = rank[max_i] - rank[max_i - 1];
		if (max_i < rank.size() - 1)
			cur_diff = min(cur_diff, rank[max_i] - rank[max_i + 1]);

		rank.erase(rank.begin() + max_i);
		answer += cur_diff;
	}

	cout << answer;


	return 0;
}
