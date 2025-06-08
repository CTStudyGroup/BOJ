#include <iostream>
#include <unordered_set>
#include <string>

using namespace std;

unordered_set<string> s;
int n,m;

void solve(string str){
	string temp;
	for (int i = 0; i < str.length(); ++i)
	{
		if (str[i]==',')
		{
			auto e=s.find(temp);
			if(e!=s.end()) s.erase(e);
			temp="";
		}else{
			temp+=str[i];
		}
	}
	auto e=s.find(temp);
	if(e!=s.end()) s.erase(e);
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin>>n>>m;
	for (int i = 0; i < n; ++i)
	{
		string temp; cin>>temp;
		s.insert(temp);
	}
	for (int i = 0; i < m; ++i)
	{
		string temp; cin>>temp;
		solve(temp);
		cout<<s.size()<<"\n";
	}
	
}