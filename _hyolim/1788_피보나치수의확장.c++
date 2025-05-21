#include <iostream>
#define DIV 1000000000
using namespace std;

long n;
long dp[1000010]={0,};

int main(){
	cin>>n;

	dp[0]=0;
	dp[1]=1;

	// 양수일 때,
	if(n>0){
		cout<<"1\n";
	}else if(n<0){
		n*=-1;
		if(n%2==0){
			cout<<"-1\n";
		}else{
			cout<<"1\n";
		}
	}else{
		cout<<"0\n";
	}

	for(int i=2;i<=n;i++){
		dp[i]=(dp[i-1]+dp[i-2])%DIV;
	}

	cout<<dp[n]%DIV;

}