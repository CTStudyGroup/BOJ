#include <iostream>
#include <vector>
using namespace std;

int arr[50001]={0,}; // 1base
vector<int> vec;
int n,k,m;
// 굳이 덱 아니어도 될 듯
// O(NK)
// 1   4 5  



void input(){
	cin>>n>>k>>m;
}

void solve(){
	int i=1;
	int cnt=0;
	int cntm=0;
	bool sig=true; // 요세푸스 일 때,
	while(vec.size()<n){
		cnt++;
		if(cnt==k){
			arr[i]=1;
			vec.push_back(i);
			cnt=0;
			cntm++;

			if(cntm==m){
				if(sig) sig=false;
				else sig=true;
				cntm=0;
			}
		}
		// 요세푸스 일 때,
		if(sig){
			// cout<<"*"<<i<<" "<<cnt<<"\n";

			// 아직 남아있는 애까지 가기	
			while(true) {
				// cout<<"i : "<<i<<" "<<vec.size()<<"\n";
				if(i==n){
					i=1;
				}else{
					i++;
				}
				if(arr[i]==0) break;
				if(vec.size()>=n) break;
			}
		}
		// 요세푸스가 아닐 때
		else{
			// cout<<"**"<<i<<" "<<cnt<<"\n";

			// 아직 남아있는 애까지 가기	
			while(true) {
				// cout<<"i : "<<i<<" "<<vec.size()<<"\n";
				if(i==1){
					i=n;
				}else{
					i--;
				}
				if(arr[i]==0) break;
				if(vec.size()>=n) break;
			}
		}

	}	
}

void output(){
	for(auto e:vec){
		cout<<e<<" ";
	}
}

int main(){
	input();
	solve();
	output();
}