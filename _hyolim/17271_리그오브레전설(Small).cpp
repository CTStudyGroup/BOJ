#include <iostream>
#define MOV 1000000007
using namespace std;

int n,m;
long dp[10001]={0,};

// 완전 DP 문제
int main(){
	cin>>n>>m;

	dp[0]=1;
	// dp[i]=i초일 때 쓸 수 있는 스킬의 개수
	for(int i=1;i<=n;i++){
		dp[i]=(dp[i]+dp[i-1])%MOV;
		if(i-m>=0){
			dp[i]=(dp[i]+dp[i-m])%MOV;
		}
	}
	for (int i = 0; i <= n; ++i)
	{
		/* code */
		cout<<dp[i]<<" ";
	}
	cout<<dp[n];
}	