#include <iostream>

using namespace std;

int sc[4]={1,5,10,50};
int check[1001]={0,};
int ans=0;
int n;

void solve(int depth,int d,int sum){
	if(depth==n){
		if(!check[sum]){
			ans++;
			check[sum]=1;
		}
		return;
	}

	for(int i=d;i<4;i++){
		solve(depth+1,i,sum+sc[i]);
	}
}

int main(){
	cin>>n;
	solve(0,0,0);
	cout<<ans;
} 