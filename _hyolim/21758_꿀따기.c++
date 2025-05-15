#include <iostream>
#include <algorithm>

using namespace std;

int n;
int honey[100001];
int sum[100001];
int answer=0;

void input(){
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>honey[i];
		sum[i]=sum[i-1]+honey[i];
	}
}

void solve(){
	// 1. 벌-꿀통-벌
	for(int i=2;i<n;i++){
		int cur=(sum[i]-sum[1])+(sum[n-1]-sum[i-1]);
		answer=max(answer,cur);
	}

	// 2. 벌-벌-꿀통
	for(int i=2;i<n;i++){
		int cur=(sum[n]-sum[1]-honey[i])+(sum[n]-sum[i]);
		answer=max(answer,cur);
	}
	
	// 3. 꿀통-벌-벌
	for(int i=2;i<n;i++){
		int cur=(sum[n-1]-honey[i])+sum[i-1];
		answer=max(answer,cur);
	}
	
}


int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
	cout<<answer;
}