#include <iostream>
#include <algorithm>
using namespace std;

int n;
long dp[101]={0,}; // v했는지 확인하는거

void solve(){
	// 초기화
	for(int i=1;i<=n;i++){
		// 그냥 입력 vs 새로운 버퍼
		dp[i]=dp[i-1]+1;

		for(int j=3;j<i;j++){
			dp[i]=max(dp[i],dp[i-j]*(j-1));
		}
	}

	cout<<dp[n];
}

int main(){
	// DP
	cin>>n;
	solve();
}