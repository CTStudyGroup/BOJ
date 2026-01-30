#include <iostream>
#include <vector>

using namespace std;

struct Info {
	int to;
	int weight;
};

int dfs(vector<bool> &visited, vector<vector<Info>> &edges, int start) {
	visited[start] = true;

	if (start != 0 && edges[start].size() == 1)
		return edges[start][0].weight;

	int need = 0;

	for (Info edge : edges[start]) {
		if (visited[edge.to])
			continue;

		need += min(edge.weight, dfs(visited, edges, edge.to));
	}

	//cout << start << " " << need << "\n";
	return need;
}

int solve() {
	int N, M;
	cin >> N >> M;

	vector<vector<Info>> edges(N);
	vector<bool> visited(N);
	for (int i = 0; i < M; i++) {
		int from, to, weight;
		cin >> from >> to >> weight;

		from--; to--;
		edges[from].push_back({ to, weight });
		edges[to].push_back({ from, weight });
	}

	return dfs(visited, edges, 0);
}

int main() {
	int T;
	cin >> T;

	while (T--) {
		cout << solve() << "\n";
	}

	return 0;
}
