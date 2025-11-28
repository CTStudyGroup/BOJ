#include <iostream>
#define MOD 1000

using namespace std;

int dp[1000001] = { 0, };
int main() {
	int a, b, c, N;
	cin >> a >> b >> c >> N;


	// dp[0]은 성체의 수
	// dp[1]는 죽은 수
	for (int i = 0; i < a; i++)
		dp[i] = 1;

	for (int day = a; day <= N; day++) {
		dp[day] = (dp[day - 1] + dp[day - a]) % MOD;

		if (b <= day)
			dp[day] = (dp[day] - dp[day - b] + MOD) % MOD;
	}

	if (N >= c)
		cout << (dp[N] - dp[N - c] + MOD) % MOD;
	else
		cout << dp[N];

	return 0;
}