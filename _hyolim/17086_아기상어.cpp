#include <iostream>
#include <queue>

using namespace std;

struct point_t{
	int y;
	int x;
};

int n,m;
int board[50][50]={0,};
int direct[8][2]={{-1,0},{-1,1},{-1,-1},{0,1},{0,-1},{1,0},{1,1},{1,-1}};
queue<point_t> q;
int visited[50][50]={0,};

void input(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>>board[i][j];
			if(board[i][j]){
				q.push({i,j});
				visited[i][j]=1;
			}
		}
	}
}

void solve(){
	if(q.empty()){
		cout<<0;
		exit(0);
	}
	for(;!q.empty();q.pop()){
		point_t temp=q.front();
		point_t next;

		for(int i=0;i<8;i++){
			next.y=temp.y+direct[i][0];
			next.x=temp.x+direct[i][1];

			if(next.y<0||next.x<0||next.y>=n||next.x>=m) continue;

			if(board[next.y][next.x]) continue;

			if(visited[next.y][next.x]) continue;

			visited[next.y][next.x]=visited[temp.y][temp.x]+1;
			q.push(next);
		}
	}
}

void output(){
	int maxA=-1;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(maxA<visited[i][j]) maxA=visited[i][j];
		}
	}
	cout<<maxA-1;
}

int main(){
	input();
	solve();
	output();
}