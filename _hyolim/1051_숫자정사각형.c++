#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int n,m;
int map[51][51]={0,};
int dp[52][52]={0,};
void input(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		string temp; cin>>temp;
		for(int j=0;j<m;j++){
			map[i][j]=temp[j]-'0';
		}
	}
}

void solve(){
	
	for(int ms=min(n,m)-1;ms>=0;ms--){
		// cout<<ms<<" \n";
		for(int i=0;i<n-ms;i++){
			for(int j=0;j<m-ms;j++){
				// cout<<i<<" "<<j<<"\n";
				// cout<<map[i][j]<<" "<<map[i][j+ms]<<" "<<map[i+ms][j]<<" "<<map[i+ms][j+ms]<<"\n";
				if(map[i][j]==map[i][j+ms]&&map[i][j]==map[i+ms][j]&&map[i][j]==map[i+ms][j+ms]){
					cout<<(ms+1)*(ms+1);
					return;
				}
			}
		}
	}
}
int main(){
	input();
	solve();
}