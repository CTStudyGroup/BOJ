#include <iostream>

using namespace std;

int N;

void solve(int n,int start,int to,int bypass){
	if(n==1){
		cout<<start<<" "<<to<<"\n";
		return;
	}

	solve(n-1,start,bypass,to);
	cout<<start<<" "<<to<<"\n";
	solve(n-1,bypass,to,start);
}
int main(){
	cin>>N;
	cout<<(1<<N)-1<<"\n";
	solve(N,1,3,2);
}