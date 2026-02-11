#include <algorithm>
#include <iostream>
#include <vector>
#define INF 987654321

using namespace std;

struct Info {
	int cost;
	int vertex;
};

void print(vector<vector<int>>& graph) {
	for (int i = 0; i < graph.size(); i++) {
		for (int j = 0; j < graph.size(); j++) {
			cout << graph[i][j] << " ";
		}
		cout << "\n";
	}
	cout << "\n";
}

void find_path(vector<vector<Info>>& graph, vector<int>& path, int from, int to) {
	int mid = graph[from][to].vertex;
	if (from == mid || mid == -1) {
		path.push_back(from);
		return;
	}
	find_path(graph, path, from, mid);
	find_path(graph, path, mid, to);
}

int main() {
	int n, m;
	cin >> n >> m;

	vector<vector<Info>> graph(n, vector<Info>(n, { INF, -1 }));
	for (int i = 0; i < m; i++) {
		int a, b, cost;
		cin >> a >> b >> cost;

		a--; b--;
		if (graph[a][b].cost > cost) {
			graph[a][b] = { cost, a };
		}
	}
	
	for (int i = 0; i < n; i++) {
		graph[i][i].cost = 0;
	}


	// 플로이드 와샬 코드인데
	// 역추적을 어떻게 하면 되는거지?
	for (int mid = 0; mid < n; mid++) {
		for (int start = 0; start < n; start++) {
			for (int end = 0; end < n; end++) {
				if (graph[start][end].cost > graph[start][mid].cost + graph[mid][end].cost) {
					graph[start][end].cost = graph[start][mid].cost + graph[mid][end].cost;
					graph[start][end].vertex = mid; // start-end까지 가는데 mid를 거치는게 빠름
				}
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << ((graph[i][j].cost != INF) ? graph[i][j].cost : 0) << " ";
		}
		cout << "\n";
	}
	/*// === [DEBUG] ===
	cout << "\n";
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << graph[i][j].vertex << " ";
		}
		cout << "\n";
	}
	cout << "\n";
	// === [DEBUG] === */

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (i == j || graph[i][j].cost == INF) {
				cout << 0 << "\n";
				continue;
			}

			vector<int> answer;
			find_path(graph, answer, i, j);
			answer.push_back(j);

			cout << answer.size() << " ";
			for (auto e : answer)
				cout << e + 1 << " ";
			cout << "\n";
		}
		//cout << "\n";
	}

	return 0;
}
