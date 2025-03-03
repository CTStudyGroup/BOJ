#include <iostream>

using namespace std;

long arr[1000001];
int t;
int n;
long answer=0;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
}

void solve(){
	long temp=arr[n-1];

	for(int i=n-2;i>=0;i--){
		if(temp>arr[i]){
			answer+=temp-arr[i];
		}else{
			temp=arr[i];
		}
	}
	cout<<answer<<"\n";
	answer=0;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin>>t;
	while(t--){
		// cout<<"-----------------\n";
		input();
		solve();
	}
}