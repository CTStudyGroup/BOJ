/*
앞자리 숫자가 더 큰 경우를 찾는다.
해당 숫자보다 바로 작은 숫자와 자리를 바꾼다.
바꾼 자리 뒷부분을 정렬시킨다.
*/

#include <iostream>
#include <algorithm>

using namespace std;

int n;
int arr[10001];
int idx=-1;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
}

void solve(){
	// 앞자리 숫자가 더 큰 경우를 찾는다.
	int i=n-1;
	while(i>0){
		if(arr[i]<arr[i-1]){
			idx=i-1;
			break;
		}
		i--;
	}

	if(idx==-1) {
		cout<<"-1";
		exit(0);
	}
	// cout<<arr[idx]<<" "<<idx<<"\n";
	int maxnum=0;
	int maxidx=0;

	// 찾은 숫자보다 바로 작은 숫자를 찾는다.
	for(int j=idx+1;j<n;j++){
		if(arr[idx]>arr[j]){
			if(maxnum<arr[j]){
				maxnum=arr[j];
				maxidx=j;
			}
		}
	}

	// cout<<maxnum<<" "<<maxidx<<"\n";
	swap(arr[idx],arr[maxidx]);
	sort(arr+idx+1,arr+n,greater<int>());

}

void output(){
	for(int i=0;i<n;i++){
		cout<<arr[i]<<" ";
	}
}
int main(){
	input();
	solve();
	output();
}