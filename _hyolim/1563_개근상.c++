#include <iostream>

using namespace std;

int n;
int divval=1000000;
long dp[1001][2][3]={0,}; // 날짜, 지각, 결석

int main(){
	cin>>n;
	dp[1][0][0]=dp[1][1][0]=dp[1][0][1]=1;

	for(int i=2;i<=n;i++){
		// 0번 지각 0번 결석
		dp[i][0][0]=(dp[i-1][0][0]+dp[i-1][0][1]+dp[i-1][0][2])%divval;
		
		// 0번 지각 1번 결석
		dp[i][0][1]=(dp[i-1][0][0])%divval;

		// 0번 지각 2번 결석
		dp[i][0][2]=dp[i-1][0][1]%divval;

		// 1번 지각 0번 결석
		dp[i][1][0]=(dp[i-1][0][0]+dp[i-1][0][1]+dp[i-1][0][2]+dp[i-1][1][0]+dp[i-1][1][1]+dp[i-1][1][2])%divval;

		// 1번 지각 1번 결석
		dp[i][1][1]=dp[i-1][1][0]%divval;

		// 1번 지각 2번 결석
		dp[i][1][2]=dp[i-1][1][1]%divval;
	}
	cout<<(dp[n][0][0]+dp[n][0][1]+dp[n][0][2]+dp[n][1][0]+dp[n][1][1]+dp[n][1][2])%divval;
}