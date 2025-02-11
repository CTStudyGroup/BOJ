#include <iostream>

using namespace std;

// 문제 유형을 모르겠다.
// dP?
// 3차원 배열 점화식 0 : 왼쪽 카드만 통에 버릴 경우, 1 : 왼쪽, 오른쪽 둘 다 버릴 경우, 2: 오른쪽 카드를 버릴 경우 
// 들어가는 값: 왼쪽카드 남아있는 수, 오른쪽 카드 남아있는 수, 현재 점수
// dp[i][j][k]=max(dp[i][j-1][0],dp[i][j-1][1],dp[i][j-1][2])+k에 달라지는 값
// 초기화 : dp[i][0][k] 전부 0

// 굳이 이럴 필요 없었음.
// dp[i][j] : i 번째까지의 왼쪽 카드와 j번째까지의 오른쪽 카드가 남아있을 때 얻을 수 있는 최대 점수
// 왼쪽 카드랑 오른쪽 카드의 개수에 따라서 점화식을 세우면 됐었음
int n;
int a[2001];
int b[2001];
int dp[2001][2001]={0,};

void input(){
	cin>>n;
	for(int i=n;i>=1;i--){
		cin>>a[i];
	}
	for(int i=n;i>=1;i--){
		cin>>b[i];
	}
}

void solve(){
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			dp[i][j]=max(dp[i-1][j-1],dp[i-1][j]); // 왼쪽 하나만 버리던가, 둘 다 버리던가
			if(a[i]>b[j]){
				//오른쪽이 더 작으면 갱신
				dp[i][j]=max(dp[i][j],dp[i][j-1]+b[j]);
			}
		}
	}
}

int main(){
	input();
	solve();
	cout<<dp[n][n];
}