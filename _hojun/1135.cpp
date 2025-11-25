#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<int>> employees;

int dfs(int parent) {

	vector<int> childTime;
	int childCnt = employees[parent].size() - 1;
	int ret = 0;

	for (auto & child : employees[parent]) {
		childTime.push_back(dfs(child));
	}

	sort(childTime.begin(), childTime.end());

	cout << parent << "의 자식들의 시간 : ";
	for (auto& time : childTime) cout << time << " ";
	cout << endl;

	for (auto& time : childTime) {
		ret = max(ret, time + childCnt--);
	}

	return ret + 1;
}

int main() {
	cin >> n;
	employees.resize(51, vector<int>());

	for (int i = 0; i < n; ++i) {
		int parent;
		cin >> parent;

		if (parent == -1) continue;

		//해당 부모를 가진 자식을 저장
		//0이 부모인 1, 2 노드를 저장함
		employees[parent].push_back(i);
	}

	cout << dfs(0);
	return 0;
}

//자식들의 걸리는 시간을 구해야함 -> dfs로 구하기
//자식들중에서 가장 시간이 많이 걸리는 자식한테 먼저 건다 -> 그래야 아래 자식한테도 가능함
//