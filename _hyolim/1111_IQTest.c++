#include <iostream>
#include <set>
#include <vector>
using namespace std;

int n;
vector<long> inVec;
set<long> answer;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		long x;
		cin>>x;
		inVec.push_back(x);
	}

}

void rec(long depth,long a,long b){
	if(depth==n-1){ //n-1이랑 n은 비교할 수 없으니
		answer.insert(inVec[depth]*a+b);
		return;
	}

	// cout<<inVec[depth]*a+b<<" "<<inVec[depth+1]<<"\n";
	if(inVec[depth]*a+b!=inVec[depth+1]) return;

	rec(depth+1,a,b);
} 

void solve(){
	if(n==1){
		cout<<"A";
		return;
	}

	for(int i=-200;i<=200;i++){
		// cout<<"*"<<i<<" "<<inVec[0]*i<<" "<<inVec[1]-(inVec[0]*i)<<"\n";
		rec(0,i,inVec[1]-(inVec[0]*i));
	}


	if(answer.empty()){
		cout<<"B";
		return;
	}

	if(answer.size()==1){
		cout<<*answer.begin();
		return;
	}
	cout<<"A";
	return;
	
}


int main(){
	input();
	solve();
}