#include <bits/stdc++.h>

using namespace std;

int main() {

	int n; cin >> n;
	stack<pair<int, int>> stk;
	int ans = 0;

	for (int i = 0; i < n; i++) {
		int idx, val;
		cin >> idx >> val;

		if (stk.empty()) {
			stk.push({ idx, val });
			continue;
		}

		int stkVal = stk.top().second;
		while (stkVal > val)
		{
			ans++;
			stk.pop();
			if (stk.empty()) break;
			stkVal = stk.top().second;
		}
		if (stkVal != val) {
			stk.push({ idx, val });
		}
	}

	while (!stk.empty()) {
		int stkVal = stk.top().second;
		stk.pop(); 
		if(stkVal != 0) ans++;
	}

	cout << ans;

	return 0;
}