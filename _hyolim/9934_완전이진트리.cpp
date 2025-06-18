 #include <iostream>
#include <vector>
using namespace std;

//1<=k<=10
//2^k
int input[10024];
int k;
vector<int> arr[10];
void insertTree(int depth,int start, int end) {
	
	if (start >= end) {
		return;
	}
	int mid = (start + end) / 2;
	arr[depth].push_back(input[mid]);
	insertTree(depth + 1, start, mid);
	insertTree(depth + 1, mid+1, end);

}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	cin >> k;
	
	
	int num;
	int idx = 0;
	while (cin >> num) {
		input[idx++] = num;
	}
	insertTree(0,0, idx);
	for (int i = 0; i < k; i++) {
		for (auto o : arr[i]) {
			cout << o << ' ';
		}
		cout << '\n';
	}
	return 0;
}