#include <iostream>
#include <cmath>
#include <vector>
#include <cstring>

using namespace std;

int n;
int money;
vector<int> vec;
long dp[10001]={0,};

void reset(){
	vec.clear();
	memset(dp,0,sizeof(dp));
}

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		int x;
		cin>>x;
		vec.push_back(x);
	}
	cin>>money;
}

void printDP(){
	cout<<"--dp--\n";
	for(int i=1;i<=money;i++) cout<<dp[i]<<" ";

	cout<<"\n";
}
void solve(){
	dp[0]=1;
	for(int i=0;i<n;i++){
		for(int j=vec[i];j<=money;j++){
			dp[j]+=dp[j-vec[i]];
		}
	}
	// printDP();
	cout<<dp[money]<<"\n";
}

int main(){
	int t; cin>>t;
	while(t--){
		reset();
		input();
		solve();

	}
}