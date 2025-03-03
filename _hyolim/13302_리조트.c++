#include <iostream>
#include <algorithm>
#define INF 987654321
using namespace std;

// dp를 2차원으로
// 하루권 (쿠폰&일반), 3일권 5일권, 쿠폰
int n,m;
bool check[101];
int dp[101][101]={0,};

// dp[]
void input(){
	cin>>n>>m;
	while(m--){
		int temp;
		cin>>temp;
		check[temp]=true;
	}

	for(int i=0;i<101;i++){
		for(int j=0;j<101;j++){
			dp[i][j]=INF;
		}
	}
}

int solve(int day, int cou){
	if(day>n) return 0;
	if(dp[day][cou]!=INF) return dp[day][cou];
	if(check[day]){
		dp[day][cou]=solve(day+1,cou);
		return dp[day][cou];
	}

	dp[day][cou]=min(dp[day][cou],solve(day+1,cou)+10000);
	dp[day][cou]=min(dp[day][cou],solve(day+3,cou+1)+25000);
	dp[day][cou]=min(dp[day][cou],solve(day+5,cou+2)+37000);
	if(cou>=3) dp[day][cou]=min(dp[day][cou],solve(day+1,cou-3));

	return dp[day][cou];
}

int main(){
	input();
		cout<<solve(1,0);
}