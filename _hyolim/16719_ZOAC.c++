#include <iostream>
#include <string>
#include <set>
using namespace std;

string str;
int alpha[28]={0,};
bool visited[101];
string answer="";

void solve(){
	for(int j=0;j<str.length();j++){
		set<pair<string,int>> s;
		// 하나 더 추가하기
		for(int i=0;i<str.length();i++){
			if(visited[i]) continue;
			visited[i]=true;
			string temp="";
			for(int v=0;v<str.length();v++){
				if(visited[v]) temp+=str[v];
			}
			s.insert({temp,i});
			visited[i]=false;
		}
		cout<<s.begin()->first<<"\n";
		answer=s.begin()->first;
		visited[s.begin()->second]=1;
	}
}

int main(){
	cin>>str;
	solve();
}