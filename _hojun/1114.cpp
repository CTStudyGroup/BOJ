#include <bits/stdc++.h>
#define ll long long
using namespace std;

int L, K, C;
vector<int> cuttingPoints;

int search(ll length) {
	int treeSize = L;
	int cnt = C;

	for (int i = K - 1; i >= 0 && cnt > 0; i--) {
		if (treeSize - cuttingPoints[i] > length) {
			if (cuttingPoints[i + 1] - cuttingPoints[i] > length) {  // 목표길이보다 작게 자를수 없는 조각 발견시 -1 반환
				return -1;
			}

			cnt--;
			treeSize = cuttingPoints[i + 1];
		}
	}

	if (cnt > 0) {
		treeSize = cuttingPoints[0];
	}

	if (treeSize > length) {
		return -1;
	}
	else {
		return treeSize;
	}
}

int main() {
	cin >> L >> K >> C;
	set<int> cutset;

	for (int i = 0; i < K; i++) {
		int a; cin >> a;
		cutset.insert(a);
	}

	for (int a : cutset) {
		cuttingPoints.push_back(a);
	}
	cuttingPoints.push_back(L);
	K = cuttingPoints.size() - 1;

	ll left = 0;
	ll right = L;

	while (left < right)
	{
		ll mid = (left + right) / 2;
		int point = search(mid);
		if (point >= 1) {
			right = mid;
		}
		else {
			left = mid + 1;
		}
	}
	cout << left << " " << search(left);

	return 0;
}