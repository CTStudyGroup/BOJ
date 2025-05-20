#include <iostream>

using namespace std;

int n;
int dp[1010]={0,};

int main(){
	cin>>n;
	// 초기화 
	// 상근이가 이기면 0, 창영이가 이기면 1
	dp[1]=1;
	dp[3]=1;
	
	for(int i=5;i<=n;i++){
		if(dp[i-1]==0&&dp[i-3]==0&&dp[i-4]==0) dp[i]=1;
	}

	if(dp[n]) cout<<"CY";
	else cout<<"SK";
}