#include <iostream>

using namespace std;

int arr[100001]={0,};
int n,m;

void input(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
}

bool checkIsAvailable(long num){
	long cnt=0;
	long money=0;
	for(int i=0;i<n;i++){
		// cout<<arr[i]<<" "<<money<<" "<<cnt<<"\n" ;

		if(arr[i]>num) return false;
		if(money-arr[i]<0){
			cnt++;
			money=num;
		}
		money-=arr[i];

	}
	if(money<0) return false;
	if(cnt>m) return false;
	return true;
}

void solve(){
	// 이분탐색
	long l=0;
	long r=987654321987654321;
	long mid=(l+r)/2;

	while(l<=r){
		// cout<<l<<" "<<mid<<" "<<r<<"\n";
		if(checkIsAvailable(mid)){
			// cout<<"*";
			r=mid-1;
		}else{
			l=mid+1;
		}
		mid=(l+r)/2;
	}
	cout<<l;
}

int main(){
	input();
	solve();
}