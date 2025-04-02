#include <iostream>
#include <string>

using namespace std;

int n;
long answer=0;
bool check(string temp){
	long sum=0;
	for(auto e:temp){
		sum+=e-'0';
	}
	return (sum%3==0);
}

void solve(int depth,string temp){
	if(depth==n){
		// cout<<temp<<"\n";
		if(temp[0]!='0'){
			if(check(temp)) answer++;
		}
		return;
	}
	solve(depth+1,temp+'0');
	solve(depth+1,temp+'1');
	solve(depth+1,temp+'2');
}

int main(){
	cin>>n;
	solve(0,"");
	cout<<answer;
}