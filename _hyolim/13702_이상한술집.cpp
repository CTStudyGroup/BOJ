#include <iostream>

using namespace std;

long n,k;
long arr[10002]={0,};
long l=1, r=0, mid=0;

void input(){
	cin>>n>>k;
	if(n==0||k==0) {
		cout<<0;
		exit(0);
	}
	for(int i=0;i<n;i++){
		cin>>arr[i];
		if(arr[i]>r) r=arr[i];
	}

}

// k명에게 막걸리를 다 줄 수 있는지
bool isPossible(int num){
	long sum=0;
	for(int i=0;i<n;i++){
		sum+=arr[i]/num;
		if(sum>=k) return true;
	}
	return false;
}


void solve(){
	while(l<=r){
		mid=(l+r)/2;
		if(isPossible(mid)){
			l=mid+1;
		}else{
			r=mid-1;
		}
	}
	cout<<r;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
}