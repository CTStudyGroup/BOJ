#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

struct JoinInfo {
	int weight;
	int counter_id;
	int customer_id;
};

struct ExitInfo {
	int exit_time;
	int counter_id;
	long long customer_id;
};

struct Compare {
	bool operator()(const JoinInfo& a, const JoinInfo& b) {
		if (a.weight == b.weight)
			return a.counter_id > b.counter_id;
		return a.weight > b.weight;
	}
};

bool exit_compare(const ExitInfo& a, const ExitInfo& b){
	if (a.exit_time == b.exit_time)
		return a.counter_id > b.counter_id;
	return a.exit_time < b.exit_time;
}


int main() {
	int N, k;
	cin >> N >> k;

	priority_queue<JoinInfo, vector<JoinInfo>, Compare> pq;
	for (int i = 0; i < k; i++) {
		pq.push({ 0, i + 1, -1 });
	}

	// N = 손님, k 개산대의 개수
	int id, w;
	vector<ExitInfo> exit_infos;
	for (int i = 0; i < N; i++) {
		cin >> id >> w;

		JoinInfo top = pq.top();
		pq.pop();

		// cout << id << ": " << top.counter_id << "\n";
		pq.push({ top.weight + w, top.counter_id, id });

		if (top.customer_id == -1)
			continue;

		// cout << top.weight << " " << top.counter_id << " " << top.customer_id << "\n";
		exit_infos.push_back({ top.weight, top.counter_id, top.customer_id });
	}

	while (!pq.empty()) {
		JoinInfo cur = pq.top();
		pq.pop();
		if (cur.customer_id == -1)
			continue;
		exit_infos.push_back({ cur.weight, cur.counter_id, cur.customer_id });
	}

	sort(exit_infos.begin(), exit_infos.end(), exit_compare);

	long long answer = 0;
	for (int i = 0; i < N; i++) {
		// cout << exit_infos[i].exit_time << " " << exit_infos[i].counter_id << " " << exit_infos[i].customer_id << "\n";
		answer += (exit_infos[i].customer_id * (i + 1));
	}

	cout << answer;

	return 0;
}