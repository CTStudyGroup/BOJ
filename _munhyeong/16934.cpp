#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;
	vector<string> names;
	for (int i = 0; i < N; i++) {
		string cur;
		cin >> cur;
		names.push_back(cur);
	}

	map<string, int> users;
	set<string> exists_prefix;
	vector<string> answer;
	for (int i = 0; i < N; i++) {
		string cur_name = names[i];
		users[cur_name]++;

		// 여기서 prefix 처리랑 넣을지를 미리 보자.
		bool is_inserted = false;

		if (users[cur_name] != 1) {// 이미 있는 유저
			answer.push_back(names[i] + to_string(users[cur_name]));
			is_inserted = true;
		}
		// 처음 들어온 유저인데, prefix 등록을 해야 되는 상황

		string prefix = "";
		for (auto c : cur_name) {
			prefix += c;
			if (exists_prefix.insert(prefix).second && !is_inserted) {
				answer.push_back(prefix);
				is_inserted = true;
			}
		}

		if (!is_inserted) {
			if (users[cur_name] == 1)
				answer.push_back(cur_name);
			else 
				answer.push_back(names[i] + to_string(users[cur_name]));
		}
	}

	for (int i = 0; i < N; i++) {
		cout << answer[i] << "\n";
	}
	

	return 0;
}