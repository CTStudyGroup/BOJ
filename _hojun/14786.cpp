#include <bits/stdc++.h>

using namespace std;

int main() {

	int A, B, C; cin >> A >> B >> C;

	long double left = (C - B) / (double)A, right = (C + B) / (double)A;
	long double mid;

	while (right - left > 1e-9)
	{
		mid = (left + right) / 2;

		if (sin(mid) > (C - A * mid) / B)
		{
			right = mid;
		}
		else
		{
			left = mid;
		}
	}

	cout.precision(10);
	cout << mid;

	return 0;
}