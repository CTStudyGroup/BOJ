#include <iostream>
using namespace std;

int n;
long long x;

// 전체 재료
long long  hb[51];
//패티 수
long long p[51];
long long solve(int n, long long x)
{
	if (n == 0) {
		if (x == 0) return 0;
		else if (x == 1) return 1;
	}

	if (x == 1)
		return 0; // 무조건 햄버거 번
	else if (x <= 1 + hb[n - 1])
		return solve(n - 1, x - 1);
	else if (x == 1 + hb[n - 1] + 1)
		return p[n - 1] + 1;
	else if (x <= 1 + hb[n - 1] + 1 + hb[n - 1])
		return 1 + p[n - 1] + solve(n - 1, x - 1 - hb[n - 1] - 1);
	else
		return 2 * p[n - 1] + 1;

}
int main()
{
	cin >> n >> x;

	hb[0] = 1;
	p[0] = 1;

	for (int i = 1; i <= n; ++i) {
		hb[i] = 1 + hb[i - 1] + 1 + hb[i - 1] + 1;
		p[i] = p[i - 1] + 1 + p[i - 1];
	}
	cout << solve(n, x) << "\n";
	return 0;
}
view raw