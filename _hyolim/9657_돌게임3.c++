#include <iostream>
#include <string>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);

	int n;
	cin>>n;
	string str[2]={"CY","SK"};
	int dp[1001]={0,};
	dp[1]=1;
	dp[2]=0;
	dp[3]=1;
	dp[4]=1;
	dp[5]=1;
	dp[6]=1;
	dp[7]=0;
	dp[8]=1;

	for(int i=9;i<=n;i++){
		if(!dp[i-1]||!dp[i-3]||!dp[i-4]) dp[i]=1;
	}
	cout<<str[dp[n]];
}