#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// input 에서 보드 채우고
// dfs로 안채워진 부분 수 찾기
int m,n,k;
int board[101][101]={0,};
int tempy=-1;
int tempx=-1;
int visited[101][101]={0,};
int direct[4][2]={{0,1},{1,0},{0,-1},{-1,0}};
vector<int> ans;

void input(){
	cin>>m>>n>>k;

	for(int i=0;i<k;i++){
		int y1,x1,y2,x2;
		cin>>y1>>x1>>y2>>x2;
		for(int j=y1;j<y2;j++){
			for(int k=x1;k<x2;k++){
				board[k][j]=1;
			}
		}
	}
}

void printBoard(){
	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++){
			cout<<board[i][j];
		}
		cout<<"\n";
	}
}

bool findZ(){
	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++){
			if(board[i][j]==0) {
				tempy=i;
				tempx=j;
				return true;
			}
		}
	}
	return false;
}

int dfs(int y,int x,int depth){
	visited[y][x]=1;
	board[y][x]=1;
	for(int i=0;i<4;i++){
		int ny=y+direct[i][0];
		int nx=x+direct[i][1];

		// 범위
		if(ny<0||nx<0||ny>=m||nx>=n) continue;

		// 조건
		if(board[ny][nx]) continue;

		// Visited
		if(visited[ny][nx]) continue;
		depth=dfs(ny,nx,depth+1);
	}
	return depth;

}

void solve(){
	while(findZ()){
		int d=dfs(tempy,tempx,1);
		ans.push_back(d);
	}
}

void output(){
	cout<<ans.size()<<"\n";

	sort(ans.begin(),ans.end());

	for(auto e:ans){
		cout<<e<<" ";
	}

}


int main(){
	input();
	// printBoard();
	solve();
	// printBoard();
	output();
}