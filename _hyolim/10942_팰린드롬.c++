#include <iostream>

using namespace std;

int n;
int arr[2001];
bool dp[2001][2001];

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i+1];
	}
}

void solve(){
	// dp[i][j]=dp[i+1][j-1]&&(arr[i]==arr[j])
	for(int i=1;i<=n;i++){
		dp[i][i]=true;
	}

	for(int i=1;i<=n-1;i++){
		if(arr[i]==arr[i+1]){
			dp[i][i+1]=true;
		}
	}


	for(int i=n-1;i>=1;i--){
		for(int j=i+2;j<=n;j++){
			if(arr[i]==arr[j]&&dp[i+1][j-1]){
				dp[i][j]=true;
			}
		}
	}
}

void output(){
	int m,s,e;
	cin>>m;
	for(int i=0;i<m;i++){
		cin>>s>>e;
		cout<<dp[s][e]<<"\n";
	}
}

int main(){
	input();
	solve();
	output();
}