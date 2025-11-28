#include <bits/stdc++.h>

using namespace std;

int main() {
	int a, b, d, n; cin >> a >> b >> d >> n;
	vector<int> dp(n + 1);

	for (int i = 0; i < a; ++i) dp[i] = 1;
	for (int i = a; i <= n; ++i) {
		//a번째 전에 있던 애들이 성체가 되서 분열시작
		dp[i] = (dp[i - 1] + dp[i - a]) % 1000;

		//b번째 전에 있던 애들이 늙어서 분열 불가능
		if (i >= b) {
			dp[i] = (dp[i] - dp[i - b] + 1000) % 1000;
		}
	}

	int answer = dp[n];
	//n번째에서 죽은 애들은 생명주기 d 전에 태어난 애들임
	if (n >= d) answer = (answer + 1000 - dp[n - d]) % 1000;
	cout << answer;
	return 0;
}