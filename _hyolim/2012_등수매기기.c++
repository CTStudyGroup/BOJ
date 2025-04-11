#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int n;
vector<int> pending;
long long answer=0;
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin>>n;
	for(int i=0;i<n;i++){
		int x;
		cin>>x;
		pending.push_back(x);

	}

	sort(pending.begin(),pending.end());
	int idx=1;
	// for(int i=1;i<=n;i++){
	// 	cout<<arr[i]<<" ";
	// }

	for(int i=1;i<=n;i++){
		answer+=abs(pending[i-1]-i);
	}
	cout<<answer;
}