#include <bits/stdc++.h>

using namespace std;

int main() {
	int N; cin >> N;
	vector<char> str(N);
	vector<char> ans;

	for (int i = 0; i < N; ++i) {
		cin >> str[i];
	}

	int left = 0, right = N -1;
	while (left <= right)
	{
		if (str[left] == str[right]) {
			int tl = left + 1;
			int tr = right - 1;
			bool flag = false;

			while (tl <= tr) {
				if (str[tl] < str[tr]) {
					ans.push_back(str[left++]);
					flag = true;
					break;
				}
				else if (str[tl] > str[tr]) {
					ans.push_back(str[right--]);
					flag = true;
					break;
				}
				else {
					tl++;
					tr--;
				}
			}
			if (!flag) {
				ans.push_back(str[left++]);
			}
		}
		else if (str[left] < str[right]) {
			ans.push_back(str[left++]);
		}
		else {
			ans.push_back(str[right--]);
		}
		
	}
	for (int i = 0; i < ans.size(); i++) {
		if (i != 0 && i % 80 == 0) cout << "\n";
		cout << ans[i];
	}
	return 0;
}