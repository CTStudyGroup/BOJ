#include <iostream>
#include <algorithm>

using namespace std;

int t,w;
int tree[1002]={0,};
int dp[1002][32][3]={0,};
int ans=-1;

void input(){
	cin>>t>>w;
	for(int i=1;i<=t;i++){
		cin>>tree[i];
	}
}

int isEat(int _t,int _num){
	// 둘이 같으면 1 다르면 0 반환
	return _t!=_num;
}

void solve(){
	// dp 테이블 채우기
	for(int x=1;x<=t;x++){
	    dp[x][0][1] = dp[x - 1][0][1] + (tree[x] == 1 ? 1 : 0);

		for(int y=1;y<=w;y++){
			if(x<y) break;
			if(tree[x]==1){
				dp[x][y][1]=max(dp[x-1][y-1][2],dp[x-1][y][1])+1;
				dp[x][y][2]=max(dp[x-1][y-1][1],dp[x-1][y][2]);
			}
			else{
				dp[x][y][1]=max(dp[x-1][y-1][2],dp[x-1][y][1]);
				dp[x][y][2]=max(dp[x-1][y-1][1],dp[x-1][y][2])+1;
			}
			// cout<<"x: "<<x<<" y: "<<y<<" [1] = "<<dp[x][y][1]<<"\n"; 
			// cout<<"x: "<<x<<" y: "<<y<<" [2] = "<<dp[x][y][2]<<"\n"; 

		}
	}

}

void output(){
	for(int i=0;i<=w;i++){
		ans=max({ans,dp[t][i][1],dp[t][i][2]});
	}
	cout<<ans;
}

int main(){
	input();	
	solve();
	// cout<<dp[t][w][1]<<" "<<dp[t][w][2];
	output();
	// cout<<max(dp[t][w][1],dp[t][w][2]);
}

