#include <iostream>

using namespace std;

int n;
long dp[120]={0,};



int main(){
	dp[1]=1;
	dp[2]=1;
	dp[3]=1;

	for(int i=4;i<=116;i++){
		dp[i]=dp[i-1]+dp[i-3];
	}

	cin>>n;
	cout<<dp[n];
}