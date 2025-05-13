#include <iostream>
#include <stack>
#include <string>
using namespace std;
	
stack<int> s;

void input(){
	string temp;
	cin>>temp;
	for(int i=0;i<temp.length();i++){
		if(temp[i]=='(') s.push(1);
		else s.push(0);
	}
}

void solve(){
	int cnt1=0;
	int cnt0=0;

	while(!s.empty()){
		int top=s.top();
		if(top==1){
			if(cnt0>0) cnt0--;
			else cnt1++;
		}else{
			cnt0++;
		}
		s.pop();
	}
	cout<<cnt1+cnt0;
}

int main(){
	input();
	solve();
}