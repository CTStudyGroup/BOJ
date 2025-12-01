#include <bits/stdc++.h>

using namespace std;

int pizzaSum;
int ans;

void checkPizza(int p, vector<int>& arr, vector<int>& arrCnt) {
	//피자의 개수
	for (int i = 1; i <= p; i++) {
		int sum = 0;
		for (int j = 0; j < i; j++) {
			sum += arr[j];
		}
		arrCnt[sum]++;
		//전체 피자하나를 선택
		if (sum == pizzaSum) ans++;

		if (i == p) break;
		//앞에서 줄여감
		for (int j = 1; j < p; j++) {
			sum -= arr[j - 1];
			sum += arr[(j + i - 1) % p];
			arrCnt[sum]++;
			//피자 하나에서만 가져오는 케이스 
			if (sum == pizzaSum) ans++;
		}
	}
}

int main() {
	cin >> pizzaSum;
	int a, b; cin >> a >> b;

	vector<int> pizzaA(a+1);
	vector<int> pizzaB(b+1);
	//A에서 나올 수 있는 합
	vector<int> cntA(2000001);
	//B에서 나올 수 있는 합
	vector<int> cntB(2000001);

	for (int i = 0; i < a; ++i) cin >> pizzaA[i];
	for (int i = 0; i < b; ++i) cin >> pizzaB[i];

	checkPizza(a, pizzaA, cntA);
	checkPizza(b, pizzaB, cntB);

	for (int i = 1; i < pizzaSum; i++) {
		int j = pizzaSum - i;
		ans += cntA[i] * cntB[j];
	}
	cout << ans;

	return 0;
}