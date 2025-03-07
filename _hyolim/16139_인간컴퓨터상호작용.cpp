#include <iostream>
#include <string>
#include <vector>

using namespace std;

string S;
int strl;
vector<int> str[26];
int t;

void printStr(){
	for(int i=0;i<26;i++){
		cout<<(char)('a'+i)<<": ";
		for(auto e: str[i]){
			cout<<e<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>S;
	strl=S.length();
	for(int i=0;i<strl;i++){
		str[S[i]-'a'].push_back(i);
	}
}

void solve(){
	cin>>t;

	char a;
	int l,r;
	int cnt=0;
	while(t--){
		cin>>a>>l>>r;
		cnt=0;
		for(auto e:str[a-'a']){
			if(l<=e&&e<=r) cnt++;
			if(e>r) break;
		}
		cout<<cnt<<"\n";
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	input();
	solve();
}