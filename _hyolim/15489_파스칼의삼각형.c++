#include <iostream>

using namespace std;

int r,c,w;
long dp[100][100]={0,};
void input(){
	cin>>r>>c>>w;
}

void solve(){
	dp[1][1]=1;
	for(int i=2;i<=60;i++){
		for(int j=1;j<=i;j++){
			if(j==1||j==i) dp[i][j]=1;
			else dp[i][j]=dp[i-1][j-1]+dp[i-1][j];
		}
	}

	// 계산
	// r번째 줄 c번째수
	long sum=0;
	for(int i=0;i<w;i++){ // 4번
		for(int j=0;j<i+1;j++){
			sum+=dp[r+i][c+j];
		}
	}
	cout<<sum;
}

int main(){
	input();
	solve();
}