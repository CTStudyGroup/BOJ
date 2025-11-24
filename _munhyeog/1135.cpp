#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int traversal(vector<vector<int>> &tree, int root) {
	if (tree[root].empty())
		return 0;

	vector<int> child_times;
	for (auto child : tree[root]) {
		int cur_time = traversal(tree, child);
		child_times.push_back(cur_time);
	}

	sort(child_times.begin(), child_times.end(), greater<int>());

	int time = 1;
	int max_time = 0;
	for (auto e : child_times) {
		max_time = max(max_time, time + e);
		time += 1;
	}

	return max_time;
}

int main() {
	int N;
	cin >> N;

	int answer = 0;
	vector<vector<int>> tree(N);
	for (int i = 0; i < N; i++) {
		int cur;
		cin >> cur;
		if (cur == -1)
			continue;

		tree[cur].push_back(i);
	}

	cout << traversal(tree, 0);

	return 0;
}