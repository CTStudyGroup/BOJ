#include <iostream>
#include <string>
using namespace std;

string moo="moo";
long n;
void solve(int n,int k,int len){
	int newlen=len*2+k+3;
	if(n<=3){
		cout<<moo[n-1];
		exit(0);
	}

	if(newlen<n) solve(n,k+1,newlen);
	else{
		if(n>len&&n<=len+k+3){
			if(n-len!=1) cout<<"o";
			else cout<<"m";
			exit(0);
		}else{
			solve(n-(len+k+3),1,3);
		}
	}
}

int main(){
	cin>>n;
	solve(n,1,3);
}