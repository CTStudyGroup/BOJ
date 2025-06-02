#include <iostream>
#include <algorithm>

using namespace std;

int n;
long arr[2001]={0,};
long dp[2001]={0,};
long cnt[2001]={0,};

void input(){
	cin>>n;
	for(int i=n;i>=1;i--){
		cin>>arr[i];
	}
}

void solve(){
	for(int i=1;i<=n;i++){
		for(int j=0;j<i;j++){
			if(arr[j]<arr[i]){
				dp[i]=max(dp[i],dp[j]+1);
			}
		}
	}
	
	int maxnum=0;
	for(int i=1;i<=n;i++){
		if(maxnum<dp[i]) maxnum=dp[i];
	}
	cout<<n-maxnum;
}

int main(){
	input();
	solve();
}