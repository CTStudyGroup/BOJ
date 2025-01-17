#include <iostream>

using namespace std;

int n;
int arr[10000][10000]={0,};

void addStar(int y, int x){
	arr[y][x+2]=1;

	arr[y+1][x+1]=1;
	arr[y+1][x+3]=1;

	arr[y+2][x]=1;
	arr[y+2][x+1]=1;
	arr[y+2][x+2]=1;
	arr[y+2][x+3]=1;
	arr[y+2][x+4]=1;
}

void solve(int depth,int y,int x){
	if(depth==3){
		addStar(y,x);
		return;
	}
	// cout<<depth;
	// cout<<n;
	solve(depth/2,y,x+depth/2);
	solve(depth/2,y+depth/2,x);
	solve(depth/2,y+depth/2,x+depth);	
}

void output(){
	for(int i=0;i<n;i++){
		for(int j=0;j<2*n-1;j++){
			if(arr[i][j]==1) cout<<'*';
			else cout<<' ';
		}
		cout<<'\n';
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin>>n;
	solve(n,0,0);
	output();

}