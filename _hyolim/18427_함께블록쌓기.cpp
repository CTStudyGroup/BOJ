#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#define DIV 10007

using namespace std;

int n,m,h;
vector<int> block[51];
long dp[51][1001]={0,};

void input(){
	cin>>n>>m>>h;

	string temp;
	getline(cin,temp);

	for(int i=1;i<=n;i++){
		string temp;
		getline(cin,temp);

		string tt;
		for(auto e:temp){
			if(e!=' '){
				tt+=e;
			}else{
				block[i].push_back(stoi(tt));
				tt="";
			}
		}
		block[i].push_back(stoi(tt));
	}

	// for(int i=1;i<=n;i++){
	// 	for(auto e:block[i]){
	// 		cout<<e<<" ";
	// 	}
	// 	cout<<"\n";
	// }
}

void solve(){
	// dp[0][0]=1;
	for(int i=1;i<=n;i++){
		// dp[i][j] = 각 사람마다 j까지 올릴 수 있는 방법의 수
		for(auto e:block[i]){
			for(int j=1;j<=h;j++){
				if(j<e) dp[i][j]=(dp[i][j]+dp[i-1][j])%DIV;
				else{
					dp[i][j]=(dp[i][j]+dp[i-1][j-e]+1)%DIV;
				}
				cout<<i<<" "<<j<<" "<<e<<" "<<dp[i][j]<<"\n";

			}
		}
	}
	cout<<"======\n";
	for(int i=1;i<=n;i++){
		for(int j=1;j<=h;j++){
			cout<<dp[i][j]<<" ";
		}
		cout<<"\n";
	}
}

int main(){
	input();
	solve();
}