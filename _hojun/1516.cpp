#include <bits/stdc++.h>

using namespace std;

int main() {
	int n; cin >> n;

	vector<int> times(n + 1, 0);
	vector<int> indegree(n + 1, 0);
	vector<int> dp(n + 1, 0);
	vector<vector<int>> graph(n + 1);

	vector<int> result(n + 1, 0);

	for (int i = 1; i <= n; ++i) {
		int build;
		cin >> times[i] >> build;
		while (build != -1)
		{
			indegree[i]++;
			graph[build].push_back(i);
			cin >> build;
		}
	}

	queue<int> q;
	for (int i = 1; i <= n; ++i) {
		if (indegree[i] == 0) { // 시작 건물들을 큐에
			q.push(i);
			dp[i] = times[i];
		}
	}
	while (!q.empty()) {
		int curr = q.front(); // 지금 짓는건물 curr
		q.pop();

		for (auto& next : graph[curr]) {
			if (next > 0) {
				dp[next] = max(dp[next], dp[curr] + times[next]); 
				indegree[next]--;
				//차수가 0이 되면 큐에 push하기
				if (indegree[next] == 0) { 
					q.push(next);
				}
			}
		}
	}

	for (int i = 1; i <= n; ++i)
		cout << dp[i] << endl;

	return 0;
}