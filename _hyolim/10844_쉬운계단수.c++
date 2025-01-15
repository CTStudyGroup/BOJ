#include <iostream>

using namespace std;

int n;
long dp[102][10]={0,};

void input(){
	cin>>n;
	for(int i=1;i<10;i++){
		dp[1][i]=1;
	}
}

void solve(){
	// dp 테이블 채우기
	for(int i=2;i<=100;i++){
		for(int j=0;j<10;j++){
			if(j>0){
				dp[i][j]+=dp[i-1][j-1];
			}
			if(j<9){
				dp[i][j]+=dp[i-1][j+1];
			}
			dp[i][j]%=1000000000000;
		}
	}
}

void output(){
	long ans=0;
	for(int i=0;i<=9;i++){
		ans+=dp[n][i];
		ans%=1000000000;
	}
	cout<<ans%1000000000;
}
int main(){
	input();
	solve();
	output();

}