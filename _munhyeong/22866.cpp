#include <iostream>
#include <vector>
#include <stack>

using namespace std;

struct Build {
	int height;
	int idx;
};

struct AnswerInfo {
	int cnt;
	int distance;
	int num;

	AnswerInfo() {
		cnt = 0;
		distance = 100001;
		num = -1;
	}
};

int main() {
	int N;
	cin >> N;

	vector<int> arr(N);
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	vector<AnswerInfo> answer(N);
	stack<Build> st;
	for (int i = 0; i < N; i++) {
		while (!st.empty() && st.top().height <= arr[i])
			st.pop();

		if (st.empty()) {
			st.push({ arr[i], i });
			continue;
		}

		int cur_distance = i - st.top().idx;
		if (answer[i].distance > cur_distance) {
			answer[i].distance = cur_distance;
			answer[i].num = st.top().idx;
		}
		else if (answer[i].distance == cur_distance &&
				answer[i].num > st.top().idx) {
			answer[i].num = st.top().idx;
		}
		answer[i].cnt += st.size();
		st.push({ arr[i], i });
	}

	st = stack<Build>();
	for (int i = N - 1; i >= 0; i--) {
		while (!st.empty() && st.top().height <= arr[i])
			st.pop();

		if (st.empty()) {
			st.push({ arr[i], i });
			continue;
		}

		int cur_distance = st.top().idx - i;
		if (answer[i].distance > cur_distance) {
			answer[i].distance = cur_distance;
			answer[i].num = st.top().idx;
		}
		else if (answer[i].distance == cur_distance &&
			answer[i].num > st.top().idx) {
			answer[i].num = st.top().idx;
		}
		answer[i].cnt += st.size();
		st.push({ arr[i], i });
	}

	for (auto e : answer) {
		cout << e.cnt;
		if (e.cnt)
			cout << " " << e.num + 1;
		cout << "\n";
	}

	return 0;
}