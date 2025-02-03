#include <iostream>
#include <string>
#include <set>
using namespace std;

int t;
int n;
set<string> se;

void input(){
	se.clear();
	cin>>n;
}

int res(string s){
	int summ=0;
	int temp=0;
	
	int i=0;
	bool sig=true;
	while(i<s.length()){
		// sig true 양수
		if(s[i]>'0'&&s[i]<='9'){
			temp*=10;
			temp+=s[i]-'0';
		}
		if(s[i]=='+'){
			if(sig) summ+=temp;
			else summ-= temp;
			sig=true;
			temp=0;
		}
		if(s[i]=='-'){
			if(sig) summ+=temp;
			else summ-= temp;
			sig=false;
			temp=0;
		}

		i++;
	}
	if(sig) return summ+temp;
	else return summ-temp;
}

void solve(int depth,string s){
	if(depth==n+1){
		// 0이 되는지 확인
		if(!res(s)) {
			se.insert(s);
		}
		return;
	}
	s.push_back(depth+'0');
	if(depth==n){
		solve(depth+1,s);
	}else{
		for(int i=0;i<3;i++){
			if(i==0) s.push_back('+');
			if(i==1) s.push_back(' ');
			if(i==2) s.push_back('-');
			solve(depth+1,s);
			s.erase(s.end()-1);
		}
	}

}

void output(){
	for(auto e:se){
		cout<<e<<"\n";
	}
}

int main(){
	cin>>t;
	for(int i=0;i<t;i++){
		input();
		solve(1,"");
		output();
		cout<<"\n";
	}	
}