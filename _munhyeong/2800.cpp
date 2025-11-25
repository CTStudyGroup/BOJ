#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

struct Pair {
	int open;
	int close;
};

bool compare(const Pair& a, const Pair& b) {
	return a.open < b.open;
}

set<string> answer;
string str;
void recursive(vector<Pair>& parentheses, int start_idx, vector<Pair> choosen) {
	if (parentheses.size() <= start_idx) {
		if (!choosen.empty()) {
			vector<bool> is_activate(str.size(), true);
			for (auto e : choosen) {
				is_activate[e.open] = false;
				is_activate[e.close] = false;
			}

			string output;
			for (int i = 0; i < str.size(); i++) {
				if (is_activate[i])
					output += str[i];
			}
			answer.insert(output);
		}
		return;
	}
	recursive(parentheses, start_idx + 1, choosen);
	choosen.push_back(parentheses[start_idx]);
	recursive(parentheses, start_idx + 1, choosen);
}

int main() {
	cin >> str;

	vector<Pair> parentheses;
	stack<int> st;
	for (int i = 0; i < str.size(); i++) {
		if (str[i] == '(') {
			st.push(i);
		}
		else if (str[i] == ')') {
			parentheses.push_back({ st.top(), i });
			st.pop();
		}
	}

	recursive(parentheses, 0, vector<Pair>());
	for (auto e : answer) {
		cout << e << "\n";
	}

	return 0;
}
