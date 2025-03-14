#include <iostream>
#include <cmath>

using namespace std;

int arr[302][302]={0,};
int dp[302][302]={0,};
int n,m;

void input(){
	cin>>n>>m;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
			cin>>arr[i][j];
		}
	}
}

void solve(){
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
			dp[i][j]=max(dp[i-1][j],dp[i][j-1])+arr[i][j];
		}
	}
	cout<<dp[n][m];
}

int main(){
	input();
	solve();
}