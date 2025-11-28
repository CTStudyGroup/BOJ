//먼저 현재 N
#include <bits/stdc++.h>

using namespace std;

struct customer
{
	int count;
	int index;
};

struct calc
{
	int id;
	int calcIdx;
	int time;
};

struct cmp {
	bool operator()(calc a, calc b) {
		if (a.time == b.time) {
			return a.calcIdx < b.calcIdx;
		}
		return a.time > b.time;
	}
};

struct cmp2 {
	bool operator()(customer a, customer b) {
		if (a.count == b.count) {
			return a.index > b.index;
		}
		return a.count > b.count;
	}
};

priority_queue<customer, vector<customer>, cmp2> pq_customer;
priority_queue<calc, vector<calc>, cmp> pq_out;

int main() {
	int n, k; cin >> n >> k;
	
	vector<int> calc(n);

	for (int i = 0; i < k; ++i) {
		pq_customer.push({ 0,i });
	}

	for (int i = 0; i < n; ++i) {
		int id, cnt;
		cin >> id >> cnt;

		int curCalcIndex = pq_customer.top().index;
		int curOutTime = pq_customer.top().count;

		pq_customer.pop();
		pq_customer.push({ curCalcIndex, curOutTime + cnt });
		pq_out.push({ id, curCalcIndex, curOutTime + cnt });
	}

	long long ans = 0;
	int i = 1;

	while (!pq_out.empty())
	{
		ans += (long long)pq_out.top().id * i;i++;
		pq_out.pop();
	}

	cout << ans;
	return 0;
}