#include <iostream>
#include <stack>

using namespace std;

stack<int> st[7];

int n,p;
long answer=0;

void solve(int tempn,int tempp){
	// cout<<tempn<<" "<<tempp<<"\n";

	// n번째 스택에서 tempp가 나올때까지 전부 pop
	while(!st[tempn].empty()){
		if(st[tempn].top()<=tempp) break;
		// cout<<st[tempn].top()<<" *\n";
		st[tempn].pop();
		answer++;
	}

	if(st[tempn].empty()){
		st[tempn].push(tempp);
		answer++;
		return;
	}

	if(st[tempn].top()!=tempp){
		st[tempn].push(tempp);
		answer++;
	}
	
}

int main(){
	cin>>n>>p;
	for(int i=0;i<n;i++) {
		int tempn,tempp; cin>>tempn>>tempp;
		solve(tempn,tempp);	
	}
	cout<<answer;
}