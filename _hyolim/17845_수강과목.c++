#include <iostream>
#include <algorithm>

using namespace std;

int n,k; // 최대 공부시간 // 과목 수
int importance[10001], studyTime[1001], dp[1001][10001];

void solve(){
	for(int i=1;i<=k;i++){
		for(int j=1;j<=n;j++){
			if(studyTime[i]>j) dp[i][j]=dp[i-1][j];
			else dp[i][j]=max(dp[i-1][j],dp[i-1][j-studyTime[i]]+importance[i]);
		}
	}
	cout<<dp[k][n]<<"\n";
}

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
    cin >> n >> k;
    for(int i=1; i<=k; i++) { 
      cin >> importance[i] >> studyTime[i];
    }

    dp[0][0] = 0;
    solve();
}