#include <iostream>
#include <cmath>
#include <cstring>
#define INF 10000

using namespace std;

int n,m;
int dp[10001][150];
int stone[10001]={0,};

int main(){
	cin>>n>>m;
	for (int i = 0; i < m; ++i)
	{
		int temp; cin>>temp;
		stone[temp-1]=1;
	}

	memset(dp,1,sizeof(dp));
	dp[0][0]=0;

	int temp;
	for (int i = 1; i < n; ++i)
	{	
		if(stone[i]) continue;
		for(int x=1;x<=i&&x<149;x++){
			temp=min(dp[i-x][x],min(dp[i-x][x-1],dp[i-x][x+1]));
			if(temp>=10000) continue;
			dp[i][x]=temp+1;
		}
	}


	int answer=INF;
	for (int i = 0; i < 150; ++i)
	{
		answer=min(answer,dp[n-1][i]);
	}
	if(answer==INF) cout<<-1;
	else cout<<answer;
	
}