#include <iostream>
#include <cmath>
using namespace std;

int n;
int board[33][33]={0,};
long dp[33][33][3]={0,};
long answer=0;

void input(){
	cin>>n;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cin>>board[i][j];
		}
	}
}

void solve(){
	dp[1][2][0]=1;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			if(board[i][j]) continue;
			if(dp[i][j][0]) continue;
			// 가로 - 가로
			dp[i][j][0]+=dp[i][j-1][0];

			// 가로 - 대각선
			if(board[i-1][j]==0&&board[i][j-1]==0) dp[i][j][2]+=dp[i-1][j-1][0];

			// 세로 - 세로
			dp[i][j][1]+=dp[i-1][j][1];

			// 세로 - 대각선
			if(board[i-1][j]==0&&board[i][j-1]==0) dp[i][j][2]+=dp[i-1][j-1][1];

			// 대각선 - 가로
			dp[i][j][0]+=dp[i][j-1][2];

			// 대각선 - 세로
			dp[i][j][1]+=dp[i-1][j][2];

			// 대각선 - 대각선
			if(board[i-1][j]==0&&board[i][j-1]==0) dp[i][j][2]+=dp[i-1][j-1][2];

		}
	}
	cout<<dp[n][n][0]+dp[n][n][1]+dp[n][n][2];
}

int main(){
	input();
	solve();
}