#include <iostream>
#include <deque>

using namespace std;

bool check_boundary(string sequence) {
	int N = sequence.size();
	for (int i = 1; i <= N / 2; i++) {
		string a = sequence.substr(N - i);
		string b = sequence.substr(N - (2 * i), i);
		if (a == b)
			return false;
	}
	return true;
}

string sequence;
bool recursive(string answer, const int &N) {
	// cout << answer << "\n";

	if (answer.size() == N) {
		sequence = answer;
		return true;
	}

	int last_idx = answer.size();
	answer.push_back('-1');

	bool is_true = false;
	for (int i = 1; i <= 3; i++) {
		answer[last_idx] = i + '0';
		if (check_boundary(answer)) {
			is_true = true;
			if (recursive(answer, N))
				return true;
		}
	}

	return false;
}

int main() {
	int N;
	cin >> N;

	recursive("", N);

	cout << sequence;

	return 0;
}