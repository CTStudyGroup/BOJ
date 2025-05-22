#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int dp[51][1001];
vector<int> block[51];

int main(){
	cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int N,M,H;
    cin >> N >> M >> H;
    cin.ignore();
    for(int i=1;i<=N;i++){
    	string str;
    	getline(cin,str);
    	stringstream sstr(str);
    	int num;

    	while(sstr>>num) block[i].push_back(num);
    }

    for(int i=0;i<=N;i++) dp[i][0]=1;

    for(int i=1;i<=N;i++){
    	for(int j=1;j<=H;j++){
    		for(int k=0;k<block[i].size();k++){
    			if(j>=block[i][k]) dp[i][j]=(dp[i][j]+dp[i-1][j-block[i][k]])%10007;
    		}
    		dp[i][j]=(dp[i][j]+dp[i-1][j])%10007;
    	}
    }
    cout<<dp[N][H];
}