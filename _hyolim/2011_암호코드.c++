#include <iostream>
#include <string>
#define DIV 1000000
using namespace std;


long dp[5010]={0,};
string str;

void solve(){
	if(str[0]=='0'){
		cout<<0;
		return;
	}

	dp[0]=1;
	dp[1]=1;
	for(int i=2;i<=str.length();i++){

		//26 아래일 때
		int tempnum=stoi(str.substr(i-2,2));

		if(str[i-2]!='0'&&tempnum<=26&&tempnum>0){
			dp[i]=(dp[i]+dp[i-2])%DIV;
		}
		if(str[i-1]!='0') dp[i]=(dp[i]+dp[i-1])%DIV;
	}
	// for(int i=1;i<=str.length();i++){
	// 	cout<<dp[i]<<" ";
	// }
	// cout<<"\n";
	cout<<dp[str.length()]%DIV;

}

int main(){
	getline(cin,str);
	solve();
}