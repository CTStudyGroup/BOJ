#include <iostream>

using namespace std;

long n;
long arr[101][101]={0,};
long dp[101][101]={0,};
void input(){
	cin>>n;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cin>>arr[i][j];
		}
	}
}

void solve(){
	dp[1][1]=1;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			if(i==n&&j==n) continue;
			dp[i+arr[i][j]][j]+=dp[i][j];
			dp[i][j+arr[i][j]]+=dp[i][j];
		}
	}

}

int main(){
	input();
	solve();
	cout<<dp[n][n];
}