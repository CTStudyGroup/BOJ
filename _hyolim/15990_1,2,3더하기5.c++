#include <iostream>
#define DIV 1000000009
using namespace std;

int n;
long dp[100010][4]={0,};

void reset(){
	for(int i=0;i<100010;i++) {
		dp[i][1]=0;
		dp[i][2]=0;
		dp[i][3]=0;
	}
}

void input(){
	cin>>n;
}

// 같은 수를 두 번 이상 연속해서 사용하면 안된다.
void solve(){
	// 초기화
	dp[1][1]=1;
	dp[2][2]=1;
	dp[3][1]=1; dp[3][2]=1; dp[3][3]=1;

	for(int i=4;i<=n;i++){
		// 1
		dp[i][1]=(dp[i][1]+dp[i-1][2]+dp[i-1][3])%DIV;

		// 2
		dp[i][2]=(dp[i][2]+dp[i-2][1]+dp[i-2][3])%DIV;
		
		//3
		dp[i][3]=(dp[i][3]+dp[i-3][1]+dp[i-3][2])%DIV;
	}
	cout<<(dp[n][1]+dp[n][2]+dp[n][3])%DIV<<"\n";
}

int main(){
	int t; cin>>t;
	while(t--){
		reset();
		input();
		solve();
	}	
}