#include <iostream>
#include <vector>

using namespace std;

int n,k;
long arr[1000001]={0,};
long dp[1000001]={0,};
long maxN=0;
long answer=0;

void input(){
	cin>>n>>k;

	for (int i = 0; i < n; ++i)
	{
		int x,g;
		cin>>g>>x;
		arr[x+1]=g;
		if(maxN<x+1) maxN=x+1;
	}
}

void solve(){
	for(int i=1;i<=maxN;i++){
		dp[i]=dp[i-1]+arr[i];
	}

	// for(int i=0;i<=maxN;i++){
	// 	cout<<dp[i]<<" ";
	// }
	// cout<<"\n";
	if(2*k+1>=maxN) answer=dp[maxN];
	for(int i=2*k+1;i<=maxN;i++){
		// cout<<dp[i]<<" ";
		if(answer<dp[i]-dp[i-2*k-1]) answer=dp[i]-dp[i-2*k-1];
	}
	
	cout<<answer;
}

int main(){
	input();
	solve();
}