#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int N;
	cin >> N;

	vector<long long> prefix_sum(N + 1);
	long long cur_sum = 0;
	for (int i = 1; i <= N; i++) {
		int input;
		cin >> input;
		cur_sum += input;
		prefix_sum[i] = cur_sum;
	}

	long long answer = 0;
	if (!(prefix_sum[N] % 4)) {
		if (!prefix_sum[N]) {
			long long zero_cnt = 0;
			for (int i = 1; i <= N; i++) {
				if (prefix_sum[i] == 0) zero_cnt++;
			}

			answer = (zero_cnt - 1) * (zero_cnt - 2) * (zero_cnt - 3) / 6;
		}
		else {
			long long sum = prefix_sum[N] / 4;
			long long one = 0, two = 0;
			for (int i = 1; i <= N; i++) {
				if (prefix_sum[i] == sum) one++;
				else if (prefix_sum[i] == sum * 2) two += one;
				else if (prefix_sum[i] == sum * 3) answer += two;
			}
		}
	}

	cout << answer;

	return 0;
}