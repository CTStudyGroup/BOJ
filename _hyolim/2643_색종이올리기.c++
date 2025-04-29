#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct paper{
	int h;
	int w;

	bool operator<(const paper& o)const{
		if(w==o.w){
			return h<=o.h;
		}
		return w<=o.w;
	}
};

int n;
vector<paper> vec;
int dp[101][3]={0,};

void input(){
	// 쓰뤠기용
	vec.push_back({0,0});

	cin>>n;
	for(int i=0;i<n;i++){
		int h,w;
		cin>>h>>w;
		if(h<w) vec.push_back({h,w});
		else vec.push_back({w,h});
	}
}

void solve(){
	sort(vec.begin(),vec.end());
	// for(auto e:vec){
	// 	cout<<e.h<<" "<<e.w<<"\n";
	// }

	for(int i=1;i<=n;i++){
		// 위에 올릴 수 있다면
		for(int j=1;j<=i;j++){
			if(dp[i-j][1]<=vec[i].h&&dp[i-j][2]<=vec[i].w){
				if(dp[i][0]<=dp[i-j][0]+1){
					dp[i][0]=dp[i-j][0]+1;
					dp[i][1]=vec[i].h;
					dp[i][2]=vec[i].w;
				}
			}

			if(dp[i-j][2]<=vec[i].h&&dp[i-j][1]<=vec[i].w){
				if(dp[i][0]<=dp[i-j][0]+1){
					dp[i][0]=dp[i-j][0]+1;
					dp[i][1]=vec[i].w;
					dp[i][2]=vec[i].h;
				}
			}
		}
		
	}
	// cout<<"0---\n";
	// for(int i=1;i<=n;i++){
	// 	cout<<dp[i][0]<<" "<<dp[i][1]<<" "<<dp[i][2]<<"\n";
	// }
	int answer=0;
	for(int i=1;i<=n;i++){
		if(answer<dp[i][0]){
			answer=dp[i][0];
		}
	}
	cout<<answer;
}

int main(){
	input();
	solve();
}