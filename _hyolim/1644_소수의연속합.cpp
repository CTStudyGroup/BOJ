#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int n,m;
bool num[4000001];
vector<int> pnum;
int ans=0;

void findN(){
	for(int i=2;i<=4000000;i++){
		num[i]=true;
	}

	for(int i=2;i<=sqrt(4000000);i++){
		for(int j=2*i;j<=4000000;j+=i){
			if(!num[j]) continue;
			num[j]=0;
		}
	}

	for(int i=2;i<=4000000;i++){
		if(num[i]) pnum.push_back(i);
	}

	// for(auto e:pnum){
	// 	cout<<e<<" ";
	// }
}

void solve(){
	findN();

	// 포인터를 오른쪽꺼 옮겨서 오른쪽 포인터가 가르키는거 더하고, 왼쪽꺼 빼고 
	int lp=0;
	int rp=0;
	int summ=pnum[rp];
	while(pnum[lp]<n){
		// cout<<lp<<" "<<rp<<" "<<summ<<" \n";
		if(lp==pnum.size()-1 && rp==pnum.size()-1) break;
		if(summ==n){
			ans++;
			if(lp==pnum.size()-1) continue;
			summ-=pnum[lp];
			lp++;
		}
		else if(summ>n){
			if(lp==pnum.size()-1) continue;
			summ-=pnum[lp];
			lp++;
		}else{
			if(rp==pnum.size()-1) continue;
			rp++;
			summ+=pnum[rp];
		}

	}

	int i=0;
	while(i<pnum.size()){
		if(pnum[i]==n) ans++; // 소수면 +1
		i++;
	}
	cout<<ans;
}


int main(){
	cin>>n;
	solve();
}