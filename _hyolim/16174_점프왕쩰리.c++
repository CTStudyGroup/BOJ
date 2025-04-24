#include <iostream>

using namespace std;

int map[65][65]={0,};
bool dp[65][65];
int n;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin>>map[i][j];
		}
	}
}

void solve(){
	dp[0][0]=1;

	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(!dp[i][j]) continue; // 못 갈 경우 x

			dp[i+map[i][j]][j]=1;
			dp[i][j+map[i][j]]=1;
		}
	}

	if(dp[n-1][n-1]) cout<<"HaruHaru";
	else cout<<"Hing";
}	
int main(){
	input();
	solve();
}