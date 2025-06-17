#include <iostream>
#include <algorithm>
using namespace std;

int n;
double m;
int candy[10001]={0,};
int price[10001]={0,};
int dp[10001]={0,};

void reset(){
	for(int i=0;i<10001;i++){
		candy[i]=0;
		price[i]=0;
		dp[i]=0;
	}
}

void input(){
	for(int i=1;i<=n;i++){
		cin>>candy[i];
		double p; cin>>p;
		price[i]=p*100+0.5;
	}
}

void solve(){
	int ans=0;
	// 냅색
	for(int j=1;j<=n;j++){

		for(int i=1;i<=m*100+0.5;i++){
			if(i-price[j]>=0) {
				dp[i]=max(dp[i],dp[i-price[j]]+candy[j]);
				ans=max(ans,dp[i]);
			}
			
		}
	}
	cout<<ans<<"\n";
}

int main(){
	while(1){
		cin>>n>>m;
		if(n==0&&m==0) break;
		reset();
		input();
		solve();
	}

}