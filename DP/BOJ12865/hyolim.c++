#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int n; // 물품의 수
int k; // 버틸 수 있는 무게
int arr[102][102]={ 0, }; // 각 물건의 무게+해당 물건의 가치
int dp[102][100002]={0,};

void input(){
	cin>>n>>k;
	// 1 인덱스
	for(int i=1;i<=n;i++){
		cin>>arr[i][0]>>arr[i][1];
	}

	// print
	// cout<<n<<k<<"\n";
	// for(int i=0;i<=n;i++){
	// 	// 0 : 무게 , 1 : 가치
	// 	cout<<arr[i][0]<<" "<<arr[i][1]<<"\n";
	// }
}

void solve(){
	// DP table 
	// DP[n][k] : n번째 원소 값까지 들어가고 최대 k까지 들어갈 수 있을 때 배낭에 들어갈 수 있는 최대 가치
	for(int i=1;i<=n;i++){
		for(int j=1;j<=k;j++){
			dp[i][j]=dp[i-1][j];
			// 무게가 버틸 수 있을 경우
			if(j-arr[i][0]>=0){
				dp[i][j]=max(dp[i][j],dp[i-1][j-arr[i][0]]+arr[i][1]);
			}
		}
	}
}

void output(){
	cout<<dp[n][k];
}

int main(){
	input();
	solve();
	output();
}