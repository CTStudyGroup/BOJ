#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int find_end_node(vector<pair<int, int>>& nodes) {
	int cur_top = 0;
	while (true) {
		// 1. 단 오른쪽으로 가기
		if (nodes[cur_top].second >= 0)
			cur_top = nodes[cur_top].second;
		else
			break;
	}
	return cur_top;
}

int dfs(vector<pair<int, int>> &nodes) {
	int end_node = find_end_node(nodes);
	//cout << end_node + 1 << "\n";

	vector<bool> visited(nodes.size());
	stack<int> st;
	st.push(0);

	int answer = 0;
	while (!st.empty()) {
		int top = st.top();
		st.pop();

		//cout << top + 1 << " ";
		answer++;

		bool is_inserted = false;

		if (nodes[top].second >= 0 && !visited[nodes[top].second]) {
			visited[nodes[top].second] = true;
			st.push(top);
			st.push(nodes[top].second);
			is_inserted = true;
		}

		if (nodes[top].first >= 0 && !visited[nodes[top].first]) {
			visited[nodes[top].first] = true;
			st.push(top);
			st.push(nodes[top].first);
			is_inserted = true;
		}

		if (!is_inserted) {
			if (top == end_node)
				break;
		}
	}
	return answer - 1;
}

int main() {
	int N;
	cin >> N;

	vector<pair<int, int>> nodes(N);
	for (int i = 0; i < N; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		a--; b--; c--;

		nodes[a] = { b, c };
	}

	cout << dfs(nodes);

	return 0;
}
