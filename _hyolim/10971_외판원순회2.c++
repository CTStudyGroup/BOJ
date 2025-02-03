#include <iostream>

using namespace std;

int n;
int board[11][11]={0,};
int visited[11]={0,};
long ans=21e16;
int cN;
void printB(){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin>>board[i][j];
		}
	}
}

void solve(int depth,long csum,int cnode){
	// cout<<"solve: "<<depth<<" "<<csum<<" "<<cnode<<"\n";
	if(depth==n){
		if(ans>csum) ans=csum;
		return;
	}
	if(csum>ans) return; // 백트랙킹 조건

	for(int i=0;i<n;i++){
		// 보드에 연결되어있는지 확인
		if(!board[cnode][i]) continue;
		// visited 확인
		if(depth==n-1) {
			visited[cN]=0;
		}
		else{
			visited[cN]=1;
		}
		if(visited[i]) continue;
		visited[i]=1;
		solve(depth+1,csum+board[cnode][i],i);
		visited[i]=0;
	}
}

void output(){
	cout<<ans;
}

int main(){
	input();
	// printB();
	for(int i=0;i<n;i++){
		// cout<<"=================\n";
		visited[i]=1;
		cN=i;
		solve(0,0,i);
		for(int j=0;j<n;j++){
			visited[j]=0;
		}
	}

/*
solve: 0 0 1
solve: 1 10 3
solve: 2 18 1
solve: 3 23 0
solve: 4 33 1
*/
	output();
}