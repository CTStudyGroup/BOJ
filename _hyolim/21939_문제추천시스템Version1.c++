#include <iostream>
#include <set>
#include <string>
#include <unordered_map>

using namespace std;

struct problem{
	int num;
	int level;

	bool operator<(const problem &o)const{
		if(level==o.level) return num<o.num;
		return level<o.level; 
	}
};

int n;
set<problem> s;
unordered_map<int,int> m;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		int p,l; cin>>p>>l;
		s.insert({p,l});
		m[p]=l;
	}
}

void solve(){
	string str; cin>>str;
	if(str=="add"){
		int p,l; cin>>p>>l;
		s.insert({p,l});
		m[p]=l;
	}
	if(str=="recommend"){
		int x; cin>>x;
		
		if(x==1){
			cout<<s.rbegin()->num<<"\n";
		}else{
			cout<<s.begin()->num<<"\n";
		}
	}
	if(str=="solved"){
		int p; cin>>p;
		s.erase({p,m[p]});
		m.erase(p);
	}
}

int main(){
	input();
	int m; cin>>m;
	while(m--){
		solve();
	}
}