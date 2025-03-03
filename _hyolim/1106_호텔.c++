#include <iostream>

using namespace std;

// dp[n]=min(dp[n-고객수]+홍보비용)
int c,n;
int dp[1111]={0,}; // 0:홍보 비용, 1:고객 수
int arr[22][2];
int main(){
	cin>>c>>n;

	for(int i=1;i<=n;i++){
		cin>>arr[i][0]>>arr[i][1];
	}
	// dp[0]=0;
	// dp 테이블 만들기
	for(int i=1;i<=1100;i++){
		int minN=98765432;
		for(int j=1;j<=n;j++){
			if(i-arr[j][1]<0) continue;
			// cout<<i<<" "<<j<<" "<<arr[j][1]<<" "<<dp[i-arr[j][1]]<<" "<<arr[j][0]<<"\n";
			if(minN>dp[i-arr[j][1]]+arr[j][0]){
				minN=dp[i-arr[j][1]]+arr[j][0];
			}
		}
		dp[i]=minN;
	}

	long answer=987654321;
	// 적어도..
	for(int i=c;i<=1100;i++){
		if(answer>dp[i]) answer=dp[i];
	}
	cout<<answer;
}