#include <iostream>
#include <algorithm>
using namespace std;

// 그리디하게 가장 작은 수들만 더하면 될 것 같은데
// 정렬할 것이기 때문에 N(logN)*M = 1000*3*15000

int n;
int m;
long arr[1002];

void input(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
}

void solve(){
	for(int i=0;i<m;i++){
		sort(arr,arr+n);
		long temp=arr[0]+arr[1];
		arr[0]=temp;
		arr[1]=temp;
	}
}

void output(){
	long answer=0;
	for(int i=0;i<n;i++){
		answer+=arr[i];
	}
	cout<<answer;
}

int main(){
	input();
	solve();
	output();

}