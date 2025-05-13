#include <iostream>

using namespace std;

int w,h;
long dp[101][101][2][2]={0,};
int mod=100000;
int main(){
	cin>>w>>h;
	
	for(int i=2;i<=w;i++) dp[i][1][0][0]=1;
	for(int i=2;i<=h;i++) dp[1][i][1][0]=1;

	for(int i=2;i<=w;i++){
		for(int j=2;j<=h;j++){
			dp[i][j][0][0]=(dp[i-1][j][0][0]+dp[i-1][j][0][1])%mod;
			dp[i][j][0][1]=dp[i-1][j][1][0];

			dp[i][j][1][0]=(dp[i][j-1][1][0]+dp[i][j-1][1][1])%mod;
			dp[i][j][1][1]=dp[i][j-1][0][0];

		}
	}
	cout<<(dp[w][h][0][0]+dp[w][h][1][0]+dp[w][h][0][1]+dp[w][h][1][1])%mod;

}