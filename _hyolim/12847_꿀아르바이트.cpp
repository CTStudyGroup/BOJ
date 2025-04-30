#include <iostream>

using namespace std;

// 느낌상 누적합
long arr[100001]={0,};
long answer=0;
int n,m;

void input(){
	cin>>n>>m;
	for(int i=1; i<=n;i++){
		int x; cin>>x;
		arr[i]=arr[i-1]+x;
	}

}

void solve(){
	for(int i=m;i<=n;i++){
		if(answer<arr[i]-arr[i-m]) answer=arr[i]-arr[i-m];
	}
	cout<<answer;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
}